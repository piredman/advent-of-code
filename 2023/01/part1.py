import csv
import array
import re


def loadData():
    input = 0
    with open('2023/01/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            line = row[0]
            idxs = [i for i in range(0, len(line)) if line[i].isdigit()]
            value = int(line[idxs[0]] + line[idxs[len(idxs)-1]])
            input = input + value

    return input


data = loadData()
print(data)
