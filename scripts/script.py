from concurrent.futures import ThreadPoolExecutor
import csv
import os
import re
import requests
import sys

def getMaxThreads():
    maxThreads = os.cpu_count();
    return maxThreads * 2 if maxThreads != None else 1

def task(outFilename, link):
    res = getHtmlFromServer(link)
    writeToFile(outFilename, res)

def splitHtml(linkTxt):
    htmlLst = re.split('[, \n]+', linkTxt)
    return htmlLst

def getHtmlFromServer(url):
    payload = {}
    payload["url"] = url
    res = requests.post("http://localhost:8000", data=payload)
    return res.text

def writeToFile(outFilename, content):
    with open(outFilename, "x") as outFile:
        outFile.write(content)
        
def main():
    maxThreads = getMaxThreads()
    executor = ThreadPoolExecutor(maxThreads)

    # File format: 
    #       1st column = 素材编号
    #       2nd column = 文案
    #       3rd column = 正文
    #       4th column = 参考链接
    #       5th column = 备注
    #       6th column = 选题管理-知识卡
    inputFilename = f"../in/{sys.argv[1]}"
    rows = []
    with open(inputFilename, 'r') as inputFile:
        csvReader = csv.reader(inputFile)
        header = next(csvReader)
        for row in csvReader:
            if len(row) >= 4 and row[3] != "":
                index = row[0]
                linkLst = splitHtml(row[3])
                i = 1
                for link in linkLst:
                    outFilename = f"../out/{index}_{i}.html"
                    executor.submit(task, outFilename, link)
                    i += 1
    
    executor.shutdown(wait=True, cancel_futures=False)

main()