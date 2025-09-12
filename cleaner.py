# cleaner.py
input_file = "idsp.jsonl"        # your current file
output_file = "idsp_modified.jsonl" # new fixed file

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:
    
    for line in infile:
        if not line.strip():
            continue
        # Replace wrong escaped keys back to correct ones
        line = line.replace("date\\_start", "date_start")
        line = line.replace("date\\_reported", "date_reported")
        
        # Optionally ensure it's valid JSON
        try:
            import json
            obj = json.loads(line)
            outfile.write(json.dumps(obj, ensure_ascii=False) + "\n")
        except Exception:
            print("Skipping invalid JSON:", line[:100])
