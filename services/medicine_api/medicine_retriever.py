# scripts/medicine_api/medicine_retriever.py (Best of the Best, Refined)

import requests
import logging
import re
from typing import List, Dict, Optional, Set
import argparse
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

RXNORM_API_BASE_URL = "https://rxnav.nlm.nih.gov/REST"

# This extensive map is correct and the first key to accuracy.
LOCAL_NAME_MAP = {
    # --- Painkillers / Fever Reducers (Analgesics / Antipyretics) ---
    "crocin": "Acetaminophen", "crocin advance": "Acetaminophen", "crocin 500": "Acetaminophen",
    "dolo-650": "Acetaminophen", "dolo 650": "Acetaminophen",
    "calpol": "Acetaminophen", "paracetamol": "Acetaminophen", "pcm": "Acetaminophen",
    "tylenol": "Acetaminophen",
    "combiflam": "Ibuprofen / Paracetamol",
    "brufen": "Ibuprofen", "advil": "Ibuprofen", "motrin": "Ibuprofen",
    "aspirin": "Aspirin", "ecospirin": "Aspirin", "disprin": "Aspirin",
    "voveran": "Diclofenac", "diclo": "Diclofenac",
    "nise": "Nimesulide",
    "ultracet": "Tramadol / Acetaminophen",
    "volini": "Diclofenac",
    "moov": "Diclofenac",

    # --- Antacids / Gas / Acidity ---
    "pan-d": "Pantoprazole / Domperidone", "pan d": "Pantoprazole / Domperidone",
    "pan-40": "Pantoprazole", "pan 40": "Pantoprazole", "protonix": "Pantoprazole",
    "rabekind-dsr": "Rabeprazole / Domperidone", "rabicip-d": "Rabeprazole / Domperidone",
    "omez": "Omeprazole", "omee": "Omeprazole", "prilosec": "Omeprazole",
    "aciloc": "Ranitidine", "rantac": "Ranitidine", "zinetac": "Ranitidine",
    "digene": "Antacid", "gelusil": "Antacid", "eno": "Antacid",

    # --- Antibiotics ---
    "amoxicillin": "Amoxicillin", "mox": "Amoxicillin", "moxikind-cv": "Amoxicillin / Clavulanate",
    "augmentin": "Amoxicillin / Clavulanate",
    "azithral": "Azithromycin", "zithromax": "Azithromycin", "azi": "Azithromycin",
    "cipro": "Ciprofloxacin", "ciproflox": "Ciprofloxacin", "ciplox": "Ciprofloxacin",
    "oflox": "Ofloxacin", "zenflox": "Ofloxacin", "ofloxacin": "Ofloxacin",
    "metrogyl": "Metronidazole", "flagyl": "Metronidazole",
    "doxycycline": "Doxycycline",
    "norflox": "Norfloxacin",

    # --- Anti-Allergy (Antihistamines) ---
    "cetirizine": "Cetirizine", "zyrtec": "Cetirizine", "cetzine": "Cetirizine",
    "allegra": "Fexofenadine",
    "avil": "Pheniramine",
    "levocet": "Levocetirizine",
    "montair-lc": "Montelukast / Levocetirizine", "montek-lc": "Montelukast / Levocetirizine",

    # --- Cough & Cold ---
    "benadryl": "Diphenhydramine",
    "grilinctus": "Dextromethorphan / Chlorpheniramine",
    "sinarest": "Chlorpheniramine / Paracetamol / Phenylephrine",
    "vicks action 500": "Paracetamol / Phenylephrine / Caffeine",
    "strepsils": "Amylmetacresol / Dichlorobenzyl alcohol",

    # --- Diabetes ---
    "metformin": "Metformin", "glycomet": "Metformin", "glucophage": "Metformin",
    "glimepiride": "Glimepiride", "amaryl": "Glimepiride",
    "glipizide": "Glipizide",
    "januvia": "Sitagliptin",

    # --- Blood Pressure / Heart ---
    "amlodipine": "Amlodipine", "amlong": "Amlodipine", "amlopres": "Amlodipine",
    "telma": "Telmisartan", "telmisartan": "Telmisartan",

    "losar": "Losartan", "losartan": "Losartan",
    "atorvastatin": "Atorvastatin", "atorva": "Atorvastatin", "lipitor": "Atorvastatin",
    "clopidogrel": "Clopidogrel", "clopitab": "Clopidogrel", "plavix": "Clopidogrel",

    # --- Vitamins & Supplements ---
    "neurobion": "Multivitamin", "supradyn": "Multivitamin",
    "shelcal": "Calcium / Vitamin D3",
    "liv-52": "Herbal Supplement",

    # --- Anti-Emetics (Vomiting/Nausea) ---
    "ondem": "Ondansetron", "vomikind": "Ondansetron",
    "domstal": "Domperidone",
    "stemetil": "Prochlorperazine",
}


def requests_retry_session(session=None, retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504)):
    session = session or requests.Session()
    retry = Retry(total=retries, read=retries, connect=retries, backoff_factor=backoff_factor, status_forcelist=status_forcelist)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    return session

session = requests_retry_session()


def normalize_ingredient_name(name: str) -> str:
    """
    More robustly cleans up ingredient names to their base chemical form.
    e.g., 'pantoprazole sodium' -> 'pantoprazole', 'domperidone maleate' -> 'domperidone'
    """
    return name.split(' ')[0].strip().lower()

def get_rxcui(medicine_name: str) -> Optional[str]:
    """Finds the RxCUI using the simple, proven cascade."""
    search_name = medicine_name.lower().strip()
    if search_name in LOCAL_NAME_MAP:
        search_name = LOCAL_NAME_MAP[search_name]
        logger.info(f"Local name map: '{medicine_name}' -> '{search_name}'.")
    try:
        url = f"{RXNORM_API_BASE_URL}/rxcui.json?name={search_name}"
        response = session.get(url, timeout=7)
        response.raise_for_status()
        data = response.json().get("idGroup", {})
        if data.get("rxnormId"):
            return data["rxnormId"][0]
        logger.info(f"No direct match for '{search_name}', trying approximate.")
        url = f"{RXNORM_API_BASE_URL}/approximateTerm.json?term={search_name}&maxEntries=1"
        response = session.get(url, timeout=7)
        response.raise_for_status()
        data = response.json().get("approximateGroup", {})
        if data.get("candidate"):
            return data["candidate"][0]["rxcui"]
    except requests.RequestException as e:
        logger.error(f"API request failed for '{medicine_name}': {e}")
    return None

def get_medicine_info(rxcui: str) -> Optional[Dict]:
    """Retrieves and filters information using the allrelated endpoint."""
    try:
        url = f"{RXNORM_API_BASE_URL}/rxcui/{rxcui}/allrelated.json"
        response = session.get(url, timeout=10)
        response.raise_for_status()
        data = response.json().get("allRelatedGroup", {})
        
        info = { "primary_name": "N/A", "generic_names": set(), "brand_names": set() }
        
        if data.get("conceptGroup"):
            for group in data.get("conceptGroup", []):
                tty, concepts = group.get("tty"), group.get("conceptProperties", [])
                
                # PIN/IN = Precise Ingredient / Ingredient. Apply normalization here.
                if tty in ["IN", "PIN"] and concepts:
                    info["generic_names"].update(normalize_ingredient_name(c['name']) for c in concepts)
                
                # BN = Brand Name
                if tty == "BN" and concepts:
                    info["brand_names"].update(c['name'].split(" ")[0] for c in concepts)
        
        # Fallback to get name if still missing
        if info['generic_names']:
            url_name = f"{RXNORM_API_BASE_URL}/rxcui/{rxcui}/property.json?propName=RxNorm Name"
            info["primary_name"] = session.get(url_name, timeout=7).json().get('propConceptGroup', {}).get('propConcept', [{}])[0].get('propValue', 'N/A')

        return info
    except requests.RequestException as e:
        logger.error(f"API info retrieval failed for RxCUI {rxcui}: {e}")
        return None

def retrieve_and_summarize(medicine_name: str) -> str:
    rxcui = get_rxcui(medicine_name)
    if rxcui:
        details = get_medicine_info(rxcui)
        if details and details["generic_names"]:
            generic_str = " + ".join(sorted([i.title() for i in details["generic_names"]]))
            details["brand_names"].add(medicine_name.title())
            brands_str = ", ".join(sorted(list(details["brand_names"]))[:7])
            if len(details["brand_names"]) > 7: brands_str += ", ..."
            summary = [
                f"=== Medicine Information: {medicine_name.title()} ===",
                f"🧾 **Active Ingredient(s):** {generic_str}",
                f"💊 **Common Brand Names/Alternatives:** {brands_str}", "---",
                "⚠️ **Safety Note:** This is for reference only. Always consult a healthcare professional."
            ]
            return "\n".join(summary)
    return f"Sorry, I couldn't find detailed information for '{medicine_name}'. Please check the spelling."

def compare_medicines(name1: str, name2: str) -> str:
    logger.info(f"Starting comparison: '{name1}' vs. '{name2}'")
    
    details1 = get_medicine_info(get_rxcui(name1))
    details2 = get_medicine_info(get_rxcui(name2))

    if not all([details1, details2, details1.get("generic_names"), details2.get("generic_names")]):
        missing = [n for n, d in zip([name1, name2], [details1, details2]) if not d or not d.get("generic_names")]
        return f"Sorry, I could not find ingredient information for: **{', '.join(missing)}**."
    
    ing1_set, ing2_set = details1["generic_names"], details2["generic_names"]
    ing1_str = " + ".join(sorted([i.title() for i in ing1_set]))
    ing2_str = " + ".join(sorted([i.title() for i in ing2_set]))
    
    common = ing1_set.intersection(ing2_set)
    unique_to_1 = ing1_set - common
    unique_to_2 = ing2_set - common
    
    key_difference = "They contain different primary active ingredients."
    if common:
        if unique_to_1:
            key_difference = (f"Both contain **{', '.join(i.title() for i in common)}**. However, **{name1.title()}** "
                              f"has an additional ingredient: **{', '.join(i.title() for i in unique_to_1)}**.")
        elif unique_to_2:
            key_difference = (f"Both contain **{', '.join(i.title() for i in common)}**. However, **{name2.title()}** "
                              f"has an additional ingredient: **{', '.join(i.title() for i in unique_to_2)}**.")
        else:
            key_difference = "They contain the same primary active ingredients."
            
    if 'domperidone' in unique_to_1 or 'domperidone' in unique_to_2:
        key_difference += " Domperidone is an anti-sickness agent that helps manage nausea and vomiting."

    return "\n".join([f"=== Comparison: {name1.title()} vs. {name2.title()} ===",
                      f"🧾 **Active Ingredients:**", f"  • **{name1.title()}:** {ing1_str}",
                      f"  • **{name2.title()}:** {ing2_str}", "---",
                      f"💊 **Key Difference:** {key_difference}", "---",
                      "⚠️ **Safety Note:** Use medication only as prescribed by a doctor."])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("medicines", nargs='+')
    args = parser.parse_args()
    query = " ".join(args.medicines)
    parts = re.split(r'\s+vs\s+', query, flags=re.IGNORECASE)
    if len(parts) == 2: print(compare_medicines(parts[0], parts[1]))
    else: print(retrieve_and_summarize(query))