# clean_corpus.py (Auto-Fix Version)

import json
import logging
import os

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# --- FILE PATHS ---
INPUT_FILE = "knowledge_base/corpus.jsonl"
OUTPUT_FILE = "knowledge_base/corpus_clean.jsonl"
BACKUP_FILE = "knowledge_base/corpus_original_backup.jsonl"

def sanitize_jsonl_with_autofix():
    """
    Reads the input .jsonl file, attempts to auto-fix common JSON errors
    (specifically incorrect backslashes), validates each line, and writes
    the corrected lines to a new, clean file.
    """
    # Create a backup of the original file just in case.
    if os.path.exists(INPUT_FILE):
        os.rename(INPUT_FILE, BACKUP_FILE)
        logger.info(f"Original file backed up to: {BACKUP_FILE}")
    else:
        logger.error(f"FATAL: Input file not found at {INPUT_FILE}")
        return

    line_count = 0
    malformed_count = 0
    
    try:
        with open(BACKUP_FILE, 'r', encoding='utf-8') as infile, \
             open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
            
            logger.info(f"Starting sanitization of {BACKUP_FILE}...")

            for i, line in enumerate(infile, 1):
                stripped_line = line.strip()
                if not stripped_line:
                    continue

                # --- AUTO-FIX ATTEMPT ---
                # The most common error is unescaped backslashes.
                # In Python, we need to replace '\\' with '\\\\', which becomes '\' -> '\\' in the final JSON string.
                fixed_line = stripped_line.replace('\\', '\\\\')

                try:
                    # Try to parse the FIXED line to ensure it's valid JSON
                    json_obj = json.loads(fixed_line)
                    # If it's valid, write it back out, correctly formatted
                    json.dump(json_obj, outfile)
                    outfile.write('\n') # Add the newline to maintain .jsonl format
                    line_count += 1
                except json.JSONDecodeError:
                    malformed_count += 1
                    logger.warning(f"Skipped malformed line at original line number {i} even after auto-fix.")
                    logger.debug(f"Problem line was: {stripped_line}")

        # The clean file is the new original
        os.rename(OUTPUT_FILE, INPUT_FILE)

        logger.info("Sanitization and auto-fix complete.")
        logger.info(f"Total valid lines processed and written: {line_count}")
        if malformed_count > 0:
            logger.warning(f"Total malformed lines that could not be auto-fixed: {malformed_count}")
        logger.info(f"The original file '{INPUT_FILE}' has now been cleaned and corrected.")

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        # Restore from backup in case of catastrophic failure
        os.rename(BACKUP_FILE, INPUT_FILE)
        logger.error("Restored original file from backup.")


if __name__ == '__main__':
    sanitize_jsonl_with_autofix()