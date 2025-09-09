# scripts/medicine_retriever.py (Definitive, Human-Readable Version)

import requests
import logging
import re
from typing import List, Dict, Optional, Set
import argparse

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- CONFIGURATION ---
RXNORM_API_BASE_URL = "https://rxnav.nlm.nih.gov/REST"

# GREATLY EXPANDED LOCAL NAME MAP (Indian & International Focus)
# This acts as a high-accuracy cache before hitting the API.
LOCAL_NAME_MAP = {
    # Analgesics / Antipyretics
    "crocin": "Acetaminophen", "crocin advance": "Acetaminophen",
    "dolo-650": "Acetaminophen", "dolo 650": "Acetaminophen",
    "paracetamol": "Acetaminophen", "pcm": "Acetaminophen",
    "tylenol": "Acetaminophen",
    "combiflam": "Ibuprofen / Paracetamol",
    "brufen": "Ibuprofen", "advil": "Ibuprofen", "motrin": "Ibuprofen",
    "aspirin": "Aspirin", "ecospirin": "Aspirin", "disprin": "Aspirin",
    "voveran": "Diclofenac", "nise": "Nimesulide",
    "ultracet": "Tramadol / Acetaminophen",

    # Antacids / PPIs
    "pan-d": "Pantoprazole / Domperidone", "pan d": "Pantoprazole / Domperidone",
    "pan-40": "Pantoprazole", "pan 40": "Pantoprazole", "protonix": "Pantoprazole",
    "rabekind-dsr": "Rabeprazole / Domperidone",
    "omee": "Omeprazole", "prilosec": "Omeprazole",
    "digene": "Antacid", "gelusil": "Antacid",

    # Antibiotics
    "amoxycillin": "Amoxicillin", "augmentin": "Amoxicillin / Clavulanate",
    "azithral": "Azithromycin", "zithromax": "Azithromycin", "azi": "Azithromycin",
    "cipro": "Ciprofloxacin", "oflox": "Ofloxacin",
    "metrogyl": "Metronidazole",
    
    # Anti-allergics
    "cetirizine": "Cetirizine", "zyrtec": "Cetirizine",
    "allegra": "Fexofenadine",
    "avil": "Pheniramine",

    # Diabetes
    "metformin": "Metformin", "glycomet": "Metformin",

    # Blood Pressure / Heart
    "amlodipine": "Amlodipine", "amlong": "Amlodipine",
    "atorvastatin": "Atorvastatin", "lipitor": "Atorvastatin",

    # Others
    "ondem": "Ondansetron",
}

# --- HELPER FUNCTIONS ---

def get_rxcui(medicine_name: str) -> Optional[str]:
    """
    Intelligently finds the RxCUI for a medicine. Prefers simple, common forms.
    Strategy: 1. Local Map -> 2. Exact Match (for common types) -> 3. Fuzzy Match
    """
    search_name = medicine_name.lower().strip()
    
    # 1. High-accuracy local map lookup
    if search_name in LOCAL_NAME_MAP:
        search_name = LOCAL_NAME_MAP[search_name]
        logger.info(f"Local name found. Mapping '{medicine_name}' to '{search_name}'.")

    # 2. Direct match, but search for common, simple drug forms first
    # (SCD = Semantic Clinical Drug, SBD = Semantic Branded Drug, GPCK = Generic Pack)
    term_types = "SCD+SBD+GPCK+BPCK"
    try:
        url = f"{RXNORM_API_BASE_URL}/rxcui.json?name={search_name}&tty={term_types}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("idGroup", {}).get("rxnormId"):
            rxcui = data["idGroup"]["rxnormId"][0]
            logger.info(f"Direct match found for '{search_name}' (type {term_types}): RxCUI {rxcui}")
            return rxcui

        # 3. Fallback to fuzzy search if no direct clinical drug is found
        logger.info(f"No direct match. Trying approximate search for '{search_name}'...")
        url = f"{RXNORM_API_BASE_URL}/approximateTerm.json?term={search_name}&maxEntries=1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("approximateGroup", {}).get("candidate"):
            rxcui = data["approximateGroup"]["candidate"][0]["rxcui"]
            logger.info(f"Approximate match found for '{search_name}': RxCUI {rxcui}")
            return rxcui
    
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed for '{medicine_name}': {e}")
    
    return None


def get_medicine_info(rxcui: str) -> Optional[Dict]:
    """Retrieves and intelligently filters information for a given RxCUI."""
    try:
        url = f"{RXNORM_API_BASE_URL}/rxcui/{rxcui}/allrelated.json"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json().get("allRelatedGroup", {})
        
        info = {
            "rxcui": rxcui,
            "primary_name": "Unknown",
            "generic_names": set(),
            "brand_names": set(),
            "forms": set()
        }

        # Find the most likely primary name for the queried concept
        primary_name_response = requests.get(f"{RXNORM_API_BASE_URL}/rxcui/{rxcui}.json?allsrc=1", timeout=5).json()
        info["primary_name"] = primary_name_response.get('idGroup', {}).get('name', 'Unknown')

        for group in data.get("conceptGroup", []):
            tty = group.get("tty")
            concepts = group.get("conceptProperties", [])
            
            # IN: Ingredient, PIN: Precise Ingredient
            if tty in ["IN", "PIN"]:
                info["generic_names"].update(c['name'] for c in concepts)
            
            # BN: Brand Name, SBD: Semantic Branded Drug
            if tty in ["BN", "SBD"]:
                # Filter for simple names, avoid long complex ones
                simple_brands = [c['name'] for c in concepts if " / " not in c['name'] and len(c['name']) < 25]
                info["brand_names"].update(simple_brands)

            # DFG: Dose Form Group (e.g., "Oral Tablet Form")
            if tty == "DFG":
                # Clean up the names for readability
                cleaned_forms = {c['name'].replace(" Form", "").replace("Oral ", "") for c in concepts}
                info["forms"].update(cleaned_forms)
        
        # Ensure the primary name is in the brand names list if it acts as one
        if info["primary_name"] and info["primary_name"] not in info["generic_names"]:
            info["brand_names"].add(info["primary_name"].split(" [")[0])

        return info

    except requests.exceptions.RequestException as e:
        logger.error(f"API info retrieval for RxCUI {rxcui} failed: {e}")
    return None

def summarize_medicine_info(info: Dict) -> str:
    """Formats the structured info into a clean, human-readable summary."""
    name = info.get('primary_name', '').split(' [')[0] # Clean up name like [Advil]
    
    generic_names = " / ".join(sorted(list(info["generic_names"]))) or "Not specified"
    
    # Show a limited, relevant number of brand names
    brand_names = sorted(list(info["brand_names"]))
    display_brands = ", ".join(brand_names[:5])
    if len(brand_names) > 5:
        display_brands += ", ..."
        
    forms = ", ".join(sorted(list(info["forms"]))) or "Not specified"
    
    combinations = set()
    for brand in info.get("brand_names", set()):
        if "/" in brand:
            parts = {p.strip().split(" ")[0] for p in brand.split("/")}
            combinations.update(parts - info["generic_names"])

    combo_text = f"🤝 **Often Combined With:** {', '.join(sorted(list(combinations)))}" if combinations else ""
    
    summary = [
        f"=== Medicine Information: {name} ===",
        f"🧾 **Generic Name(s):** {generic_names}",
        f"💊 **Common Brand Names:** {display_brands}",
        f"📦 **Available Forms:** {forms}",
        combo_text,
        "---",
        "⚠️ **Safety Note:** This is for informational purposes only. Always consult a doctor before use. Overdose or incorrect use can be harmful."
    ]
    return "\n".join(filter(None, summary))


def retrieve_and_summarize(medicine_name: str) -> str:
    """End-to-end function to find and summarize a single medicine."""
    rxcui = get_rxcui(medicine_name)
    if rxcui:
        info = get_medicine_info(rxcui)
        if info:
            return summarize_medicine_info(info)
    
    return f"Sorry, I couldn’t find '{medicine_name}' in the database. Please check the spelling or try a generic name."

def compare_medicines(name1: str, name2: str) -> str:
    """Fetches info for two medicines and provides a clear comparison."""
    logger.info(f"Starting comparison: '{name1}' vs. '{name2}'")
    
    info1 = get_medicine_info(get_rxcui(name1)) if get_rxcui(name1) else None
    info2 = get_medicine_info(get_rxcui(name2)) if get_rxcui(name2) else None
    
    if not all([info1, info2]):
        missing = [n for n, i in zip([name1, name2], [info1, info2]) if not i]
        return f"Sorry, I couldn't find information for: **{', '.join(missing)}**. Please check the spelling."

    ingredients1_set = info1["generic_names"]
    ingredients2_set = info2["generic_names"]

    ingredients1_str = " + ".join(sorted(list(ingredients1_set)))
    ingredients2_str = " + ".join(sorted(list(ingredients2_set)))
    
    diff1 = ingredients1_set - ingredients2_set
    diff2 = ingredients2_set - ingredients1_set

    key_difference = ""
    if diff1:
        key_difference = f"**{info1['primary_name'].split(' [')[0]}** contains **{', '.join(diff1)}**, which is not in {info2['primary_name'].split(' [')[0]}."
    elif diff2:
        key_difference = f"**{info2['primary_name'].split(' [')[0]}** contains **{', '.join(diff2)}**, which is not in {info1['primary_name'].split(' [')[0]}."
    else:
        key_difference = "Both medicines contain the same primary active ingredient(s)."
        
    if "Domperidone" in key_difference:
        key_difference += " Domperidone is an anti-sickness medicine that also helps with bloating and stomach discomfort."

    summary = [
        f"=== Comparison: {name1.title()} vs. {name2.title()} ===",
        f"🧾 **Active Ingredients:**",
        f"  • **{name1.title()}:** {ingredients1_str}",
        f"  • **{name2.title()}:** {ingredients2_str}",
        "---",
        f"💊 **Key Difference:** {key_difference}",
        f"📦 **Forms:** Both are commonly available as oral tablets or capsules.",
        "---",
        "⚠️ **Safety Note:** Use under medical guidance only. Differences in inactive ingredients can affect individuals differently. Avoid self-medication."
    ]
    return "\n".join(summary)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and compare medicine information.")
    parser.add_argument("medicines", nargs='+', help="One or two medicine names. Use 'vs' for comparison.")
    
    args = parser.parse_args()
    query = " ".join(args.medicines)

    # Use a more robust regex to handle spaces around "vs"
    match = re.search(r'\s+vs\s+', query, re.IGNORECASE)
    
    if match:
        parts = re.split(match.re, query, maxsplit=1)
        if len(parts) == 2:
            print(compare_medicines(parts[0], parts[1]))
        else:
            print("Usage: python script.py 'medicine1 vs medicine2'")
    else:
        print(retrieve_and_summarize(query))