import sys
import os
import shutil
import time

# Taking input from user
source_dir = sys.argv[1]  
dest_dir = sys.argv[2]

# Defining the backup function
def backup_file(source_dir, dest_dir):

    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        if os.path.isfile(source_path):
            # If it's a file, copy it directly
            dest_path = os.path.join(dest_dir, filename)
        else:
            # If it's a directory, append a timestamp to the directory name
            name, ext = os.path.splitext(filename)
            timestamp = time.strftime("%Y%m%d%H%M%S")
            dest_path = os.path.join(dest_dir, f"{name}_{timestamp}{ext}")

        try:
            shutil.copy2(source_path, dest_path)  # Copy with metadata
            print(f"Copied '{filename}' to '{dest_path}'")
        except Exception as e:
            print(f"Error: Could not copy file '{filename}': {e}")

# Run the backup function
backup_file(source_dir, dest_dir)