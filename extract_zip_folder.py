import py7zr
import os

# List of your .7z folders from the uploaded image
folders_to_extract = [
    "batch_20230912_part1-001.7z",
    "batch_20230912_part2-001.7z",
    "batch_20230919_part1-001.7z",
    "batch_20230919_part2-001.7z",
    "batch_20231027_part1-001.7z",
    "batch_20231027_part2-001.7z"
]

# Specify the path to the directory where you want to extract the contents
extract_path = "/path/to/directory"

# Ensure the extract_path exists
if not os.path.exists(extract_path):
    os.makedirs(extract_path)

# Loop through each folder and extract its contents
for folder in folders_to_extract:
    try:
        with py7zr.SevenZipFile(folder, mode='r') as archive:
            archive.extractall(path=extract_path)
        print(f"Extracted {folder} successfully.")
    except Exception as e:
        print(f"Failed to extract {folder}: {e}")

print("Extraction complete.")
