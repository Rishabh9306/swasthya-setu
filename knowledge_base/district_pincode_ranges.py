# knowledge_base/district_pincode_ranges.py

# This is the master data file mapping Odisha districts to their known pincode prefixes.
# The structure is { "DistrictName": {"prefixes": ["prefix1", ...], "hq_pincode": "..."} }.
# This is a robust one-to-many mapping.
ODISHA_DISTRICT_MAP = {
    "Angul":        {"prefixes": ["759"], "hq_pincode": "759122"},
    "Balangir":     {"prefixes": ["767"], "hq_pincode": "767001"},
    "Balasore":     {"prefixes": ["756"], "hq_pincode": "756001"},
    "Bargarh":      {"prefixes": ["768"], "hq_pincode": "768028"},
    "Bhadrak":      {"prefixes": ["756"], "hq_pincode": "756100"},
    "Boudh":        {"prefixes": ["762"], "hq_pincode": "762001"},
    "Cuttack":      {"prefixes": ["753", "754"], "hq_pincode": "753001"},
    "Deogarh":      {"prefixes": ["768"], "hq_pincode": "768108"},
    "Dhenkanal":    {"prefixes": ["759"], "hq_pincode": "759001"},
    "Gajapati":     {"prefixes": ["761"], "hq_pincode": "761200"},
    "Ganjam":       {"prefixes": ["760", "761"], "hq_pincode": "761001"},
    "Jagatsinghpur":{"prefixes": ["754"], "hq_pincode": "754103"},
    "Jajpur":       {"prefixes": ["755"], "hq_pincode": "755001"},
    "Jharsuguda":   {"prefixes": ["768"], "hq_pincode": "768201"},
    "Kalahandi":    {"prefixes": ["766"], "hq_pincode": "766001"},
    "Kandhamal":    {"prefixes": ["762"], "hq_pincode": "762101"},
    "Kendrapara":   {"prefixes": ["754"], "hq_pincode": "754211"},
    "Keonjhar":     {"prefixes": ["758"], "hq_pincode": "758001"},
    "Khordha":      {"prefixes": ["751", "752"], "hq_pincode": "751003"},
    "Koraput":      {"prefixes": ["763", "764"], "hq_pincode": "764001"},
    "Malkangiri":   {"prefixes": ["764"], "hq_pincode": "764045"},
    "Mayurbhanj":   {"prefixes": ["757"], "hq_pincode": "770002"},
    "Nabarangpur":  {"prefixes": ["764"], "hq_pincode": "764059"},
    "Nayagarh":     {"prefixes": ["752"], "hq_pincode": "752070"},
    "Nuapada":      {"prefixes": ["766", "767"], "hq_pincode": "767001"},
    "Puri":         {"prefixes": ["752"], "hq_pincode": "752020"},
    "Rayagada":     {"prefixes": ["765"], "hq_pincode": "765001"},
    "Sambalpur":    {"prefixes": ["768"], "hq_pincode": "768001"},
    "Subarnapur":   {"prefixes": ["767"], "hq_pincode": "767017"},
    "Sundargarh":   {"prefixes": ["769", "770"], "hq_pincode": "770001"}
}

# Invert the map for efficient lookup: {"prefix": [("DistrictName", "HQPincode"), ...]}
PINCODE_PREFIX_TO_DISTRICTS = {}
for district, data in ODISHA_DISTRICT_MAP.items():
    hq_pincode = data["hq_pincode"]
    for prefix in data["prefixes"]:
        if prefix not in PINCODE_PREFIX_TO_DISTRICTS:
            PINCODE_PREFIX_TO_DISTRICTS[prefix] = []
        PINCODE_PREFIX_TO_DISTRICTS[prefix].append((district, hq_pincode))