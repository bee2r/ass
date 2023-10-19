#!/usr/bin/python3

import shutil
import os

source_directory = "/home/oluwo/Documents"

destination_directory = "/home/oluwo/Downloads/ass/newass"

file_extension = ".txt"

if not os.path.exists(source_directory):
    print(f"Source directory '{source_sirectory}' does not exist.")
else:
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for filename in os.listdir(source_directory):
        source_file = os.path.join(source_directory, filename)

        if os.path.isfile(source_file) and filename.endswith(file_extension):
            destination_file = os.path.join(destination_directory, filename)
            shutil.copy(source_file, destination_file)
            print(f"Copied '{filename}' to '{destination_directory}'")

print("Copying complete.")
