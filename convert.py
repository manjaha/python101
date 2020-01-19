import csv
import json
import os
import sys

#  python convert.py D:\Python\Python101\user_details.csv D:\Python\Python101\user_details.json

csv_filepath = sys.argv[1]
json_filepath = sys.argv[2]

if os.path.isfile(csv_filepath):
    with open(csv_filepath, 'r') as f:
        csv_data = csv.DictReader(f, quotechar='"')
        with open(json_filepath, 'w') as json_file:
            for row in csv_data:
                row['password'] = '****'
                json.dump(row, json_file)
                json_file.write('\n')
else:
    print(f"'{csv_filepath}' does not exist")
