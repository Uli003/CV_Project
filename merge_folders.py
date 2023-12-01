import os
import shutil

def merge_folders(src, dst):
    for src_dir, dirs, files in os.walk(src):
        dst_dir = src_dir.replace(src, dst, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.rename(dst_file, dst_file + '_duplicate')
            shutil.move(src_file, dst_dir)

source_folder1 = '/media/tgw/aos/Part1'
source_folder2 = '/media/tgw/aos/Part2'
destination_folder ='/media/tgw/aos/dataset'

# Ensure the directory exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Merge the two folders
merge_folders(source_folder1, destination_folder)
merge_folders(source_folder2, destination_folder)

print("Folders have been merged.")
