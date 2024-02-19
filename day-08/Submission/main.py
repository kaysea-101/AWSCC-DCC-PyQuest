# import csv python module
# same syntax as txt
'''
CSV Functions
1. Reader and Writer
2. DictReader and DictWriter

'''
import csv

with open('day-08\example1.csv', 'r') as file:
  csv_reader = csv.reader(file)
  
  next(csv_reader) # skip header row
  
  # this is how you print a csv
  
  for line in csv_reader:
    
  # check the length of lines before accessing elements prevent IndexError
    if len(line ) >0:
     print(line[0]) # display column 1(also add next(reader) above  the for
  
  
'''
JSON Functions
1. json.load = read
2. json.dumps = write
'''
import json

with open('day-08\example2.json', 'r') as file:
  json_reader = json.load(file) # display as is 
  
  out = json.dumps(json_reader, indent = 3) # to print by indentation
  print(out)