#!/usr/bin/env python3
# djvu2mask
# Janusz S. Bień and ChatGPT 2024

import os
import subprocess
import sys


def extract_masks(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    # Loop through all .djvu files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".djvu"):
            djvu_file = os.path.join(directory, filename)
            base_name = os.path.splitext(djvu_file)[0]
            tiff_file = f"{base_name}_mask.tiff"

            # Step 1: Extract the mask
            subprocess.run(["ddjvu", "-format=tiff", "-mode=mask", djvu_file, tiff_file])
            subprocess.run(["identify",  tiff_file])

            print(f"Processed {djvu_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 djvu2mask.py <directory_path>")
    else:
        directory = sys.argv[1]
        extract_masks(directory)
