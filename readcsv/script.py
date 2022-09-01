import csv
import requests
import sys

filename = f"../in/{sys.argv[1]}"
rows = []
with open(filename, 'r') as file :
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader :
        index = row[0]

        try :
            int(index)
        except :
            continue

        output = f"../out/{index}.html"
        link = row[3]
        payload = {}
        payload["index"] = index
        payload["url"] = link
        res = requests.post("http://localhost:8000", data=payload)
        # with open(output, "xb") as file:
        #     file.write(res.content)
