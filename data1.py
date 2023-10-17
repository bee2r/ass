#!/usr/bin/python3 
import csv

csv_file = "data.csv"

total = 0
count = 0

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if "Score" in row:
            try:
                score = float(row["Score"])
                total += score
                count += 1
            except ValueError:
                print(f"Skipping non-numeric value: {row['Score']}")

    if count > 0:
        average = total / count
        print(f"Average score: {average}")
    else:
        print("No valid score found in colum 'Score'. ")
