#prints the first 10 rows of a csv file

import csv

with open('filename', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i in range(10):
    print reader.next()
