#!/usr/bin/python3

from datetime import datetime

date_str1 = "2023-03-15"
date_str2 = "2023-04-25"

date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

delta = date2 - date1

days_difference = delta.days

print(f"Number of days between {date_str1} and {date_str2}: {days_difference} days") 
