#Author: Varnesh Gawde
#Date 9/9/2023
#To use:
#Save the script to a file, for example, rename_files.py
#Run the script using
#----python3 rename_files.py -p /path/to/directory
import os
import argparse

def rename_files_in_serial(path):
    """Rename all files in the given directory in serial order."""
    
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    files.sort()  # Ensure consistent ordering

    for idx, filename in enumerate(files, start=1):
        # Generate new name
        extension = os.path.splitext(filename)[1]
        new_name = f"{idx}{extension}"

        # Rename file
        old_file_path = os.path.join(path, filename)
        new_file_path = os.path.join(path, new_name)
        os.rename(old_file_path, new_file_path)

        print(f"Renamed {filename} to {new_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files in serial order.")
    parser.add_argument('-p', '--path', required=True, help="Path to the directory containing files to be renamed.")
    
    args = parser.parse_args()
    rename_files_in_serial(args.path)
