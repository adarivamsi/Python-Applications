import csv
import json

with open('input.json',"r") as input_data:
    in_data = json.loads(input_data.read())

output_data = open('output.csv', 'w')
csvwriter = csv.writer(output_data)
count = 0

for i in in_data:
      if count == 0:
             header = i.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(i.values())
output_data.close()
