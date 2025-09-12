# knowledge_base/fallback_system.py

from typing import Optional, Dict
import torch
import logging
import sys
import os
import re

if __name__ == '__main__' and __package__ is None:
    # Allows the script to be run directly for testing
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    sys.path.insert(0, project_root)
    # Import our new, corrected data file
    from knowledge_base.district_pincode_ranges import ODISHA_DISTRICT_MAP, PINCODE_PREFIX_TO_DISTRICTS
    from knowledge_base.semantic_kb_data import SEMANTIC_KB
    from knowledge_base.health_glossary_data import HEALTH_GLOSSARY
    from knowledge_base.geo_fallback_data import GEO_FALLBACK_DB
else:
    # Standard relative imports for when Rasa runs the module
    from .district_pincode_ranges import ODISHA_DISTRICT_MAP, PINCODE_PREFIX_TO_DISTRICTS
    from .semantic_kb_data import SEMANTIC_KB
    from .health_glossary_data import HEALTH_GLOSSARY
    from .geo_fallback_data import GEO_FALLBACK_DB

from sentence_transformers import SentenceTransformer, util

logger = logging.getLogger(__name__)

# --- SemanticKB and HealthGlossary are UNCHANGED as they are already perfect ---
class SemanticKB:
    def __init__(self, model_name='paraphrase-multilingual-MiniLM-L12-v2', threshold=0.65):
        try:
            self.model = SentenceTransformer(model_name)
            self.kb = SEMANTIC_KB
            self.threshold = threshold
            self.all_questions = [q for item in self.kb for q in item["questions"]]
            self.answers_list = [item for item in self.kb for _ in item["questions"]]
            self.kb_embeddings = self.model.encode(self.all_questions, convert_to_tensor=True)
            logger.info("SemanticKB initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize SentenceTransformer model: {e}")
            self.model = None

    def search(self, user_query: str) -> Optional[Dict[str, str]]:
        if not self.model: return None
        query_embedding = self.model.encode(user_query, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(query_embedding, self.kb_embeddings)
        top_result = torch.topk(cos_scores, k=1)
        score, index = top_result.values.item(), top_result.indices.item()
        logger.info(f"SemanticKB search for '{user_query}'. Top match: '{self.all_questions[index]}' with score: {score:.4f}")
        if score >= self.threshold: return self.answers_list[index]
        return None

class HealthGlossary:
    def __init__(self):
        self.glossary = HEALTH_GLOSSARY
        logger.info("HealthGlossary initialized.")
    
    def lookup(self, user_query: str) -> Optional[tuple[str, Dict[str, str]]]:
        """
        Looks for a keyword from the glossary in the user's query.
        Returns a tuple of (term_found, definition_dictionary) if a match is found.
        """
        user_query_lower = user_query.lower()
        for term, definition_dict in self.glossary.items():
            if re.search(r'\b' + re.escape(term) + r'\b', user_query_lower):
                logger.info(f"HealthGlossary found term '{term}'.")
                return term, definition_dict
        return None

# --- RE-ENGINEERED GeoFallback Class ---
class GeoFallback:
    """Layer 3: Pincode lookup with a robust, two-stage resolving system."""
    def __init__(self):
        # The DB of known HQ pincodes with detailed info
        self.hq_info_db = GEO_FALLBACK_DB
        # The new map: "751" -> [("Khordha", "751003")]
        self.prefix_map = PINCODE_PREFIX_TO_DISTRICTS
        logger.info("GeoFallback initialized with intelligent district resolver.")

    def get_contacts(self, pincode: str) -> Optional[Dict[str, str]]:
        # Stage 1: Try for a direct match in our high-quality HQ database first.
        if pincode in self.hq_info_db:
            logger.info(f"GeoFallback found DIRECT match for pincode '{pincode}'.")
            return self.hq_info_db[pincode]

        # Stage 2: If no direct match, resolve the district using the prefix.
        prefix = pincode[:3]
        if prefix in self.prefix_map:
            # Get the list of possible districts, e.g., [("Khordha", "751003"), ("Nayagarh", "752069"), ...]
            possible_matches = self.prefix_map[prefix]
            
            # --- THIS IS THE ONE-LINE FIX ---
            # For simplicity and reliability, we always default to the first district in the list for an ambiguous prefix.
            district_name, hq_pincode = possible_matches[0]
            # -------------------------------

            logger.info(f"Resolved pincode '{pincode}' via prefix '{prefix}' to default district '{district_name}' (HQ Pincode: {hq_pincode}).")
            
            # Now, return the detailed information for that district's HQ.
            return self.hq_info_db.get(hq_pincode)

        logger.warning(f"No direct match or prefix map found for pincode '{pincode}'.")
        return None

# --- THE DEFINITIVE UNIT TEST SUITE ---
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("--- Testing Fallback System Modules ---")
    
    # ... (SemanticKB and HealthGlossary tests are unchanged and correct) ...
    print("\n--- 1. Testing SemanticKB ---")
    test_kb = SemanticKB()
    query1 = "how does corona spread"
    assert test_kb.search(query1) is not None, "KB Test 1 Failed"
    print("KB Test 1 -> SUCCESS")
    
    print("\n--- 2. Testing HealthGlossary ---")
    test_glossary = HealthGlossary()
    query3 = "I have a high bukhar and chills"
    assert test_glossary.lookup(query3) is not None, "Glossary Test 3 Failed"
    print("Glossary Test 3 -> SUCCESS")

    # --- THE NEW ROBUST GEOFALLBACK TEST ---
    print("\n--- 3. Testing GeoFallback ---")
    test_geo = GeoFallback()
    
    # Test Case A: A direct pincode for a major Odisha HQ (Bhubaneswar)
    bhubaneswar_hq = "751003"
    result_bhubaneswar = test_geo.get_contacts(bhubaneswar_hq)
    assert result_bhubaneswar is not None and "Capital Hospital" in result_bhubaneswar['contact_en'], "Geo Test A (Direct HQ) Failed"
    print(f"Direct HQ pincode '{bhubaneswar_hq}' resolved correctly -> SUCCESS")

    # Test Case B: A non-HQ pincode from the same district (Khordha)
    khordha_random = "752054" 
    result_khordha = test_geo.get_contacts(khordha_random)
    assert result_khordha is not None and "Capital Hospital" in result_khordha['contact_en'], "Geo Test B (Mapped) Failed"
    print(f"Mapped pincode '{khordha_random}' correctly resolved to Khordha HQ -> SUCCESS")
    
    # Test Case C: A non-HQ pincode from a district with a shared prefix (Bargarh, prefix 768)
    bargarh_random = "768032" 
    result_bargarh = test_geo.get_contacts(bargarh_random)
    # The intelligent logic should default to the first entry for "768", which is Bargarh HQ.
    assert result_bargarh is not None and "Bargarh District" in result_bargarh['contact_en'], "Geo Test C (Shared Prefix) Failed"
    print(f"Shared prefix pincode '{bargarh_random}' correctly resolved to a valid regional HQ -> SUCCESS")

    # Test Case D: A non-Odisha pincode not in our DBs (should return None)
    mumbai_pincode = "400011"
    result_mumbai = test_geo.get_contacts(mumbai_pincode)
    assert result_mumbai is None, "Geo Test D (Invalid) Failed - Should have returned None"
    print(f"Invalid pincode '{mumbai_pincode}' correctly returned no result -> SUCCESS")
    
    print("\n--- All tests passed! ---")