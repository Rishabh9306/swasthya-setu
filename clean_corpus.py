# clean_corpus.py (Definitive, All-in-One Auto-Fix Version)

import json
import logging
import os
import re

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# --- FILE PATHS ---
INPUT_FILE = "knowledge_base/corpus.jsonl"
OUTPUT_FILE = "knowledge_base/corpus_clean.jsonl"
BACKUP_FILE = "knowledge_base/corpus_original_backup.jsonl"

def sanitize_jsonl_comprehensive():
    """
    Reads, cleans, and validates a .jsonl file. It intelligently fixes both
    insufficiently and excessively escaped backslashes, making it robust
    and safe to run multiple times (idempotent).
    """
    if not os.path.exists(INPUT_FILE):
        logger.error(f"FATAL: Input file not found at {INPUT_FILE}. Nothing to do.")
        return
        
    try:
        os.rename(INPUT_FILE, BACKUP_FILE)
        logger.info(f"Original file backed up to: {BACKUP_FILE}")
    except OSError as e:
        logger.error(f"Could not create backup file: {e}")
        return

    lines_processed = 0
    lines_fixed = 0
    lines_skipped = 0
    
    try:
        with open(BACKUP_FILE, 'r', encoding='utf-8') as infile, \
             open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
            
            logger.info(f"Starting comprehensive sanitization of {BACKUP_FILE}...")

            for i, line in enumerate(infile, 1):
                original_line = line.strip()
                if not original_line:
                    continue

                lines_processed += 1
                was_fixed = False
                
                # --- AUTO-FIX STAGE 1: Handle Over-Escaping ---
                # Repeatedly replace '\\\\' with '\\' until no more changes occur.
                # This converges '\\\\\\\\' -> '\\\\' -> '\\'.
                # This is safer than a single replacement.
                sanitized_line = original_line
                while '\\\\' in sanitized_line:
                    sanitized_line = sanitized_line.replace('\\\\', '\\')
                
                if sanitized_line != original_line:
                    was_fixed = True

                # --- AUTO-FIX STAGE 2: Handle Under-Escaping ---
                # Now, find any remaining single backslash that isn't a valid escape char.
                # This regex finds a backslash that is NOT followed by another
                # backslash, a quote, or common JSON escape characters.
                final_fixed_line = re.sub(r'\\(?![\\"/bfnrt])', r'\\\\', sanitized_line)

                if final_fixed_line != sanitized_line:
                    was_fixed = True
                
                try:
                    # Validate the final, corrected line.
                    json_obj = json.loads(final_fixed_line)
                    # Write it out cleanly to ensure consistent formatting.
                    json.dump(json_obj, outfile)
                    outfile.write('\n')
                    if was_fixed:
                        lines_fixed += 1
                        logger.info(f"Fixed backslash issue on original line {i}.")
                except json.JSONDecodeError:
                    # If it still fails, the line has a non-backslash JSON error.
                    lines_skipped += 1
                    logger.warning(f"Skipped truly malformed JSON line at original line {i}.")
                    logger.debug(f"Problem line was: {original_line}")

        # Promote the clean file to become the new original.
        os.rename(OUTPUT_FILE, INPUT_FILE)
        # You can optionally remove the backup file here if you're confident.
        # os.remove(BACKUP_FILE) 

        logger.info("Sanitization complete.")
        logger.info(f"Total lines processed: {lines_processed}")
        logger.info(f"Total lines that required fixing: {lines_fixed}")
        if lines_skipped > 0:
            logger.warning(f"Total malformed lines that were skipped: {lines_skipped}")
        logger.info(f"The file '{INPUT_FILE}' is now clean and correct.")

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        # Automatically restore from the backup in case of any critical failure.
        os.rename(BACKUP_FILE, INPUT_FILE)
        logger.error("Restored original file from backup due to the error.")


if __name__ == '__main__':
    sanitize_jsonl_comprehensive()