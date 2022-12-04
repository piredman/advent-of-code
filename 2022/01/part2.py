import csv
import array

def loadData():
    numberData = array.array('i', [])
    numberData.append(0)
    with open('input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            if len(row) == 0:
                numberData.append(0)
            else:
                numberData[len(numberData) - 1] += int(row[0])

    return numberData


data = loadData()
sorted = sorted(data)
topThree = sorted[-1] + sorted[-2] + sorted[-3]
print(sorted)
print(topThree)