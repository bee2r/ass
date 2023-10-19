#!/usr/bin/python3

import shutil

input_file = "input.txt"


output_file = "output.txt"

try:
    with open(input_file, "r") as file:
        file_content = file.read()

    with open(output_file, "w") as file:
        file.write(file_content)

    print(f"Content from {input_file} copied to {output_file}")
except FileNotFoundError:
    print(f"{input_file} not found. Make sure the file exists. ")
except Exception as e:
    print(f"An error occurred: {str(e)}")
