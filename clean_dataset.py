import os
import shutil

# Path to the directory containing the dataset
source_directory = '/path/to/directorydataset'
# Path to the directory where incomplete batch files will be moved
incomplete_directory = '/path/to/directoryincomplete_batches'

# check if  incomplete_directory exists
if not os.path.exists(incomplete_directory):
    os.makedirs(incomplete_directory)

# Function to generate a list of expected filenames for a batch
def expected_files_for_batch(batch_prefix):
    expected_files = [f"{batch_prefix}_GT_pose_0_thermal.png", f"{batch_prefix}_Parameters.txt"]
    expected_files += [f"{batch_prefix}_pose_{i}_thermal.png" for i in range(11)]  # poses 0 to 10
    return expected_files

# Iterate over the files and collect files that belong to each batch
batches = {}
for filename in os.listdir(source_directory):
    # Extract batch prefix (e.g. '0_0', '0_1', etc.)
    if "pose" in filename or "Parameters" in filename or "GT" in filename:
        batch_prefix = "_".join(filename.split("_")[:2])
        batches.setdefault(batch_prefix, []).append(filename)

# Check each batch for completeness and move incomplete ones
for batch_prefix, files in batches.items():
    expected_files = expected_files_for_batch(batch_prefix)
    if not all(f in files for f in expected_files):
        # If not all expected files are present, move the files to the incomplete directory
        for file in files:
            shutil.move(os.path.join(source_directory, file), incomplete_directory)
        print(f"Moved incomplete batch {batch_prefix} to the incomplete folder.")

print("Processing complete.")
