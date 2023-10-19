#!/usr/bin/python3

import os

current_directory = os.getcwd()

files = []
directories = []

for item in os.listdir(current_directory):
    if os.path.isfile(item):
        files.append(item)
    elif os.path.isdir(item):
        directories.append(item)
        
    print("Files:")
    for file in files:
        print(file)

    print("\nDirectories:")
    for directory in directories:
        print(directory)
