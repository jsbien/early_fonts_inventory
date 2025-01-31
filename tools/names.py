import os
import csv
import re

# The script processes filenames in the 'DjVu' directory, which follow the pattern:
# <printer>-<font>_PT<fascicule>_<plate>. The extracted components are stored in 'names.csv'.
#
# - <printer>: An alphabetic string (may contain non-ASCII characters)
# - <font>: Starts with a two-digit number, possibly with additional postfixes
# - <fascicule>: A two-digit number
# - <plate>: A three-digit number
#
# The output CSV will have the following columns:
# number,file_name,printer,font,fascicule,plate
#
# The 'number' column will contain sequential two-digit numbers starting from 01.

# Define the directory containing the files
DJVU_DIR = "DjVu"
OUTPUT_CSV = "names.csv"

# Define the file name regex pattern
FILENAME_PATTERN = re.compile(
    r"(?P<printer>[\w\-]+)-(?P<font>\d{2}[^\s_]*)_PT(?P<fascicule>\d{2})_(?P<plate>\d{3})"
)

def parse_filenames(directory):
    """Parses filenames in the specified directory and extracts components."""
    results = []
    for filename in os.listdir(directory):
        match = FILENAME_PATTERN.match(filename)
        if match:
            parsed_entry = match.groupdict()
            parsed_entry["filename"] = filename  # Add the full file name
            results.append(parsed_entry)
        else:
            print(f"Skipped file: {filename} (Does not match pattern)")
    return results

def sort_parsed_data(data):
    """Sorts the parsed data in a logical order:
    1. Alphabetically by printer name
    2. Numerically by the two-digit font prefix
    3. By full font string (for secondary ordering)
    4. Numerically by fascicule
    5. Numerically by plate
    """
    return sorted(
        data,
        key=lambda x: (
            x["printer"],                       # Sort by printer alphabetically
            int(re.search(r"\d+", x["font"]).group()),  # Extract and sort font numerically
            x["font"],                          # Secondary sort by font string
            int(x["fascicule"]),                # Sort fascicule numerically
            int(x["plate"])                     # Sort plate numerically
        )
    )

def write_to_csv(output_path, data):
    """Writes the parsed data to a CSV file with a sequential 'number' field."""
    with open(output_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(["number", "filename", "printer", "font", "fascicule", "plate"])
        # Write rows with a sequential number field
        for idx, entry in enumerate(data, start=1):
            writer.writerow([
                f"{idx:02}",                 # Zero-padded number
                entry["filename"],           # Full file name
                entry["printer"],            # Printer
                entry["font"],               # Font
                entry["fascicule"],          # Fascicule
                entry["plate"]               # Plate
            ])

def main():
    # Ensure the directory exists
    if not os.path.isdir(DJVU_DIR):
        print(f"Directory '{DJVU_DIR}' does not exist. Please create it and add the files.")
        return

    # Parse filenames
    parsed_data = parse_filenames(DJVU_DIR)

    if not parsed_data:
        print(f"No valid filenames found in directory '{DJVU_DIR}'.")
        return

    # Sort the parsed data
    sorted_data = sort_parsed_data(parsed_data)

    # Write to CSV
    write_to_csv(OUTPUT_CSV, sorted_data)
    print(f"Sorted data has been written to '{OUTPUT_CSV}'.")

if __name__ == "__main__":
    main()
