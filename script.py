import csv
import requests
import sys

filename = sys.argv[1]
rows = []
with open(filename, 'r') as file :
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader :
        try :
            index = int(row[0])
            link = row[3]
        except :
            continue