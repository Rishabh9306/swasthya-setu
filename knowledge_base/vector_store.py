# knowledge_base/vector_store.py (Definitive Production Version for .jsonl)

import json
import os
import logging
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Optional

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- CONFIGURATION ---
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
CORPUS_FILE = os.path.join(os.path.dirname(__file__), "corpus.jsonl") # Corrected to .jsonl
INDEX_FILE = os.path.join(os.path.dirname(__file__), "corpus.index")

# --- GLOBAL IN-MEMORY STORE ---
model: Optional[SentenceTransformer] = None
corpus: Optional[List[Dict]] = None
faiss_index: Optional[faiss.Index] = None

def _load_corpus_from_jsonl(file_path: str) -> List[Dict]:
    """
    Efficiently and correctly loads data from a JSON Lines (.jsonl) file.
    """
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1): # Start counting lines from 1 for logging
                line = line.strip()
                if line:
                    try:
                        data.append(json.loads(line))
                    except json.JSONDecodeError:
                        logger.warning(f"Skipping malformed JSON on line {i}: {line}")
    except FileNotFoundError:
        logger.error(f"FATAL: Corpus file not found at {file_path}. Cannot proceed.")
        return []
    return data

def build_vector_store():
    """
    Builds and saves a robust FAISS index specifically for small-to-medium corpora.
    """
    logger.info(f"Loading corpus from {CORPUS_FILE}...")
    local_corpus = _load_corpus_from_jsonl(CORPUS_FILE)
    if not local_corpus:
        logger.error("Build failed: Corpus is empty or could not be read.")
        return

    texts = [doc.get("text", "") for doc in local_corpus]
    if not any(texts):
        logger.error("FATAL: Corpus contains no 'text' fields.")
        return

    logger.info(f"Loading sentence embedding model '{MODEL_NAME}'...")
    local_model = SentenceTransformer(MODEL_NAME)

    logger.info(f"Encoding {len(texts)} corpus documents into vectors...")
    embeddings = local_model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
    
    # BEST PRACTICE for ACCURACY: Normalize embeddings for reliable similarity search.
    faiss.normalize_L2(embeddings)
    
    d = embeddings.shape[1]
    
    # THE CORRECT INDEX FOR THIS CORPUS SIZE: IndexFlatL2 provides the most
    # accurate (brute-force) search, which is ideal for datasets under ~10k entries.
    logger.info(f"Building FAISS IndexFlatL2 with dimension {d}...")
    local_index = faiss.IndexFlatL2(d)
    local_index.add(embeddings)

    logger.info(f"Saving FAISS index to {INDEX_FILE}...")
    faiss.write_index(local_index, INDEX_FILE)
    logger.info(f"Successfully built and saved vector store. Total documents indexed: {local_index.ntotal}")

def load_vector_store():
    """Loads the index, corpus, and model into memory for the action server."""
    global model, corpus, faiss_index
    if faiss_index: return

    try:
        if not all(os.path.exists(f) for f in [INDEX_FILE, CORPUS_FILE]):
             raise FileNotFoundError
             
        logger.info(f"Loading FAISS index from {INDEX_FILE}...")
        faiss_index = faiss.read_index(INDEX_FILE)
        
        logger.info(f"Loading corpus data from {CORPUS_FILE}...")
        corpus = _load_corpus_from_jsonl(CORPUS_FILE)
            
        logger.info(f"Loading sentence embedding model '{MODEL_NAME}'...")
        model = SentenceTransformer(MODEL_NAME)
        
        logger.info(f"Vector store loaded. Index contains {faiss_index.ntotal} vectors.")

    except Exception as e:
        logger.error(f"Could not load vector store. RAG search will be disabled. Error: {e}")
        logger.warning(f"Please build the index first by running from your project root: python -m knowledge_base.vector_store")
        faiss_index = None

def search_corpus(query: str, top_k: int = 1) -> Optional[str]:
    """Searches the corpus and returns the best matching text."""
    if not all([model, faiss_index, corpus]):
        logger.warning("Vector store not loaded, search aborted.")
        return None

    query_embedding = model.encode([query])
    faiss.normalize_L2(query_embedding)
    
    distances, indices = faiss_index.search(query_embedding, top_k)
    
    # For normalized L2, distance from 0 (identical) to 2 (opposite).
    # A threshold of 0.8 is a good balance of relevance and coverage.
    DISTANCE_THRESHOLD = 0.8 

    if distances.size > 0 and distances[0][0] < DISTANCE_THRESHOLD:
        best_match_index = indices[0][0]
        result_doc = corpus[best_match_index]
        logger.info(f"Corpus search success. Query: '{query}'. Match ID: {result_doc['id']}, Dist: {distances[0][0]:.4f}")
        return result_doc.get('text')
    else:
        logger.info(f"Corpus search found no confident match for '{query}'. Closest distance: {distances[0][0] if distances.size > 0 else 'N/A'}")
        return None

if __name__ == '__main__':
    build_vector_store()