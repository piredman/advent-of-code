import csv
import array


def loadData():
    numberData = array.array('i', [])
    numberData.append(0)
    with open('2022/01/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            if len(row) == 0:
                numberData.append(0)
            else:
                numberData[len(numberData) - 1] += int(row[0])

    return numberData


data = loadData()
sorted = sorted(data)
largest = sorted[-1]
print(sorted)
print(largest)
