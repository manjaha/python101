import os, sys, csv

#  python readcsv.py example.csv "Trait Stack"

filepath = sys.argv[1]
column = sys.argv[2]

if os.path.isfile(filepath):
    with open(os.path.basename(filepath), 'r') as f:
        data = csv.DictReader(f, quotechar='"')
        headers = data.fieldnames
        if column not in headers:
            print(f"'{column}' does not exist")
        else:
            for row in data:
                print(row[column])
else:
    print(f"'{filepath}' does not exist")
