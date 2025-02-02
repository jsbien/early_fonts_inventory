import os
import sys
import cv2
import numpy as np
from datetime import datetime

# Script version
VERSION = "5.0"

def log_message(log_file, message):
    """Helper function to write messages to the log file."""
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now()} - {message}\n")
    print(message)  # Immediate feedback

def split_into_chunks(image, output_dir, file_basename, log_file):
    """Split the image into chunks using vertical gaps and save them."""
#    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Assuming input images are already binary
#    binary = gray
    binary = image

    # Log the shape and pixel values of the binary image
#    log_message(log_file, f"Binary image shape: {binary.shape}")
#    log_message(log_file, f"Unique pixel values in binary image: {np.unique(binary)}")

    gaps = find_vertical_gaps(binary, log_file)
#    log_message(log_file, f"Detected gaps: {gaps}")

    chunk_number = 0
    prev_gap_end = 0

    for gap_start, gap_end in gaps:
        # Extract the chunk between the previous gap and the current gap
        chunk_image = binary[:, prev_gap_end:gap_start]
        if chunk_image.shape[1] > 0:  # Ignore empty chunks
            padded_chunk = cv2.copyMakeBorder(chunk_image, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=255)

            chunk_number += 1
            chunk_dir = os.path.join(output_dir, os.path.splitext(file_basename)[0] + "_chunks")
            os.makedirs(chunk_dir, exist_ok=True)

            output_path = os.path.join(chunk_dir, f"{os.path.splitext(file_basename)[0]}_chunk_{chunk_number:02d}.png")
            cv2.imwrite(output_path, padded_chunk)

            log_message(log_file, f"Chunk {chunk_number}: Columns [{prev_gap_end}:{gap_start}] saved to {output_path}")

        prev_gap_end = gap_end + 1

    # Handle the last chunk after the final gap
    if prev_gap_end < binary.shape[1]:
        chunk_image = binary[:, prev_gap_end:]
        padded_chunk = cv2.copyMakeBorder(chunk_image, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=255)

        chunk_number += 1
        chunk_dir = os.path.join(output_dir, os.path.splitext(file_basename)[0] + "_chunks")
        os.makedirs(chunk_dir, exist_ok=True)

        output_path = os.path.join(chunk_dir, f"{os.path.splitext(file_basename)[0]}_chunk_{chunk_number:02d}.png")
        cv2.imwrite(output_path, padded_chunk)

        log_message(log_file, f"Final chunk {chunk_number}: Columns [{prev_gap_end}:{binary.shape[1]}] saved to {output_path}")

    if chunk_number == 0:
        log_message(log_file, f"No chunks detected for file: {file_basename}")

    return chunk_number

def find_vertical_gaps(binary, log_file):
    """Find vertical gaps composed of columns of white pixels."""
    height, width = binary.shape
    gaps = []

    in_gap = False
    gap_start = 0

    for x in range(width):
        if np.all(binary[:, x] == 255):  # Column is fully white
            if not in_gap:
                gap_start = x
                in_gap = True
        else:
            if in_gap:
                gaps.append((gap_start, x - 1))
#                log_message(log_file, f"Gap found: Columns [{gap_start}:{x - 1}]")
                in_gap = False

    if in_gap:  # Handle gap ending at the last column
        gaps.append((gap_start, width - 1))
#        log_message(log_file, f"Gap found: Columns [{gap_start}:{width - 1}]")

    if not gaps:
        log_message(log_file, "No gaps detected; the entire line might be one chunk.")

    return gaps

def process_image(file_path, output_dir, log_file):
    """Process a single image to extract chunks and save them with padded bounding boxes."""
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        log_message(log_file, f"ERROR: Unable to read file {file_path}")
        return

    file_basename = os.path.splitext(os.path.basename(file_path))[0]
    split_into_chunks(image, output_dir, file_basename, log_file)

def process_directory(input_dir):
    """Process all PNG files in the input directory."""
    log_file = f"chunk_extraction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_message(log_file, f"Script version: {VERSION}")
    log_message(log_file, f"Processing input directory: {input_dir}")

    output_dir = os.path.join(input_dir, "chunks")
    os.makedirs(output_dir, exist_ok=True)

    for file_name in sorted(os.listdir(input_dir)):
        if file_name.lower().endswith('.png'):
            file_path = os.path.join(input_dir, file_name)
            log_message(log_file, f"Processing file: {file_name}")
            process_image(file_path, output_dir, log_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python PT_chunks.py <input_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]

    if not os.path.isdir(input_directory):
        print(f"Error: {input_directory} is not a valid directory.")
        sys.exit(1)

    process_directory(input_directory)
    
