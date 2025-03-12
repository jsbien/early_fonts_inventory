#!/usr/bin/env python3
# masks.py
# Janusz S. Bień and ChatGPT/AskTheCode 2025

import os
import csv
import subprocess
from PyQt5.QtGui import QImage
from segment_character_table import is_black_and_white, detect_black_index

# This script processes DjVu files listed in 'names.csv' and extracts masks.
#
# - It iterates over lines in 'names.csv' (located in the root directory).
# - The second field in the CSV contains the filename of the DjVu file to be processed.
# - The DjVu files are located in the 'DjVu' directory.
# - The first field in 'names.csv' provides the number for the output filename.
# - The output filename format is 'm<number>.tiff' and is stored in the 'masks' directory.
#
# The mask extraction is done using the 'ddjvu' tool with the parameters:
#   -mode=mask -format=tiff
#
# The script ensures the extracted output is binary by using verification functions
# from `segment_character_table.py` (is_black_and_white and/or detect_black_index).
#
# If any errors occur (such as missing files, processing failures, or invalid output),
# they will be logged to the console.

# Paths
CSV_FILE = "names.csv"
DJVU_DIR = "DjVu"
MASKS_DIR = "masks"

# Ensure the output directory exists
os.makedirs(MASKS_DIR, exist_ok=True)

def process_djvu_files():
    """Processes DjVu files listed in names.csv and extracts masks as TIFF images."""
    
    # Read names.csv
    if not os.path.exists(CSV_FILE):
        print(f"Error: {CSV_FILE} not found.")
        return
    
    with open(CSV_FILE, mode="r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header
        
        for row in reader:
            try:
                number, filename = row[0], row[1]
                djvu_file = os.path.join(DJVU_DIR, filename)
                output_file = os.path.join(MASKS_DIR, f"m{number}.tiff")

                # Check if the DjVu file exists
                if not os.path.exists(djvu_file):
                    print(f"Warning: {djvu_file} does not exist. Skipping.")
                    continue
                
                # Run ddjvu to extract the mask
                try:
                    subprocess.run(
                        ["ddjvu", "-mode=mask", "-format=tiff", djvu_file, output_file],
                        check=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                    )
                except subprocess.CalledProcessError as e:
                    print(f"Error processing {djvu_file}: {e.stderr.decode().strip()}")
                    continue
                
                # Validate the output is binary
                if not os.path.exists(output_file):
                    print(f"Error: Output file {output_file} not created.")
                    continue
                
                # Load the output file into a QImage
                image = QImage(output_file)
                if image.isNull():
                    print(f"Warning: Could not load {output_file} as an image.")
                    continue
                
                if not is_black_and_white(image) and not detect_black_index(image):
                    print(f"Warning: Output file {output_file} is not binary.")
                
                print(f"Successfully processed {djvu_file} -> {output_file}")
            
            except IndexError:
                print(f"Error: Malformed row in CSV: {row}")
                continue

if __name__ == "__main__":
    process_djvu_files()
