import csv


with open("test.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)

print(name_records[1]["Difficulty Level"])
