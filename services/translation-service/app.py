# File: services/translation-service/app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.cloud import translate # Import the v3 client
from google.oauth2 import service_account
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import logging
from typing import Optional, List
import os

# --- Setup Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================================================
# 1. INITIALIZE CLIENTS AND MODELS
# ============================================================================
translate_client = None
parent = None
tokenizer_grammar = None
model_grammar = None
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# --- Explicitly load Google Cloud credentials for reliability ---
try:
    SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'gcp-credentials.json')
    GCP_PROJECT_ID = "swasthya-setu-472002"

    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        raise FileNotFoundError("GCP credentials file not found.")
    if not GCP_PROJECT_ID:
        raise ValueError("GCP_PROJECT_ID is not set in app.py.")
        
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    translate_client = translate.TranslationServiceClient(credentials=credentials)
    parent = f"projects/{GCP_PROJECT_ID}/locations/global"
    logger.info("Successfully initialized Google Translate V3 client.")

except Exception as e:
    logger.error("FATAL: FAILED TO INITIALIZE GOOGLE TRANSLATE CLIENT.", exc_info=True)


# --- Load Grammar Correction Model ---
try:
    model_name_grammar = "vennify/t5-base-grammar-correction"
    logger.info(f"Loading grammar correction model: {model_name_grammar}...")
    tokenizer_grammar = AutoTokenizer.from_pretrained(model_name_grammar)
    model_grammar = AutoModelForSeq2SeqLM.from_pretrained(model_name_grammar)
    model_grammar.to(DEVICE); model_grammar.eval()
    logger.info("Grammar correction model loaded successfully.")
except Exception as e:
    logger.error(f"WARNING: FAILED TO LOAD GRAMMAR MODEL.", exc_info=True)


# ============================================================================
# 2. API DATA MODELS (Using Pydantic v1.x Syntax)
# ============================================================================
class NormalizeRequest(BaseModel):
    text: str
class TranslateBackRequest(BaseModel):
    text: str
    target_language: Optional[str] = "or"
class ApiResponse(BaseModel):
    original_text: str
    detected_language: Optional[str] = None
    normalized_english: str
    translated_text: Optional[str] = None

# ============================================================================
# 3. CREATE FASTAPI APPLICATION
# ============================================================================
app = FastAPI(title="Swasthya-Bhasha V3 Service", version="3.2.0-FINAL")

# ============================================================================
# 4. DEFINE API ENDPOINTS
# ============================================================================
@app.get("/")
def read_root(): return {"status": "Swasthya-Bhasha Service is running."}

@app.post("/normalize", response_model=ApiResponse)
def normalize_and_translate(request: NormalizeRequest):
    if not translate_client:
        raise HTTPException(status_code=503, detail="Translation service is not initialized.")
    
    original_text = request.text
    
    try:
        response = translate_client.detect_language(
            parent=parent, content=original_text, mime_type="text/plain"
        )
        detected_lang = response.languages[0].language_code
        logger.info(f"Google detected language: '{detected_lang}'")
        
        if detected_lang != 'en':
            translation_response = translate_client.translate_text(
                parent=parent, contents=[original_text],
                target_language_code='en-US', source_language_code=detected_lang
            )
            normalized_english = translation_response.translations[0].translated_text
        else:
            if model_grammar:
                text_with_prefix = f"grammar: {original_text}"
                inputs = tokenizer_grammar(text_with_prefix, return_tensors='pt', padding=True).to(DEVICE)
                outputs = model_grammar.generate(**inputs, max_length=256, num_beams=5)
                normalized_english = tokenizer_grammar.decode(outputs[0], skip_special_tokens=True)
            else:
                normalized_english = original_text

    except Exception as e:
        logger.error(f"Error during /normalize endpoint: {e}", exc_info=True)
        detected_lang, normalized_english = 'en', original_text
        
    return ApiResponse(original_text=original_text, detected_language=detected_lang, normalized_english=normalized_english)

@app.post("/translate_back", response_model=ApiResponse)
def translate_to_target(request: TranslateBackRequest):
    if not translate_client:
        raise HTTPException(status_code=503, detail="Translation service is not initialized.")

    english_text = request.text
    # Get the target language from the request, default to 'or' if not provided
    target_language_code = request.target_language
    
    # A small safety check for language codes
    if target_language_code not in ['or', 'hi']:
        # If an unsupported language is requested, default to Odia
        logging.warning(f"Unsupported target language '{target_language_code}' requested. Defaulting to 'or'.")
        target_language_code = 'or'
    
    translated_text = english_text
    try:
        response = translate_client.translate_text(
            parent=parent, 
            contents=[english_text], 
            target_language_code=target_language_code # Use the variable here
        )
        translated_text = response.translations[0].translated_text
    except Exception as e:
        logger.error(f"Error during /translate_back endpoint: {e}", exc_info=True)
        # On error, return the original english text
        translated_text = english_text

    return ApiResponse(
        original_text=english_text, 
        detected_language="en", 
        normalized_english=english_text, 
        translated_text=translated_text
    )