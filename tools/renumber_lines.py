import os
import re
import shutil
import sys
from collections import defaultdict

def renumber_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Regex to match the filenames
    pattern = re.compile(r"m(\d+)_R_lines_(\d+)(?:-\d+)?\.png")

    files = [f for f in os.listdir(input_dir) if pattern.match(f)]
    files.sort()  # Ensure alphabetical order

    grouped_files = defaultdict(list)

    # Organize files by number1
    for filename in files:
        match = pattern.match(filename)
        if match:
            number1, number2 = match.groups()
            grouped_files[number1].append((filename, int(number2)))

    new_filenames = {}
    max_values = {}
    total_files = 0

    # Process each group
    for new_number1, (original_number1, file_list) in enumerate(sorted(grouped_files.items()), start=1):
        file_list.sort(key=lambda x: x[1])  # Sort by number2

        max_number2 = 0
        for new_number2, (filename, _) in enumerate(file_list, start=1):
            new_name = f"m{new_number1:02d}_R_lines_{new_number2:02d}.png"
            new_filenames[filename] = new_name
            max_number2 = max(max_number2, new_number2)
            total_files += 1

        max_values[f"m{new_number1:02d}"] = max_number2

    # Copy files with new names
    for old_name, new_name in new_filenames.items():
        shutil.copy(os.path.join(input_dir, old_name), os.path.join(output_dir, new_name))

    # Print statistics
    print("Statistics:")
    for key, max_val in max_values.items():
        print(f"{key}: Max number2 = {max_val}")
    print(f"Total files processed: {total_files}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python renumber_lines.py <input_dir> <output_dir>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    renumber_files(input_directory, output_directory)
