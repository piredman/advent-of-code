import csv
import statistics
fileName = '07/input.txt'


def loadData():
    output = []
    with open(fileName, 'r', newline='') as fileData:
        reader = csv.reader(fileData, delimiter=',')
        row = next(reader)
        output = [int(x) for x in row]

    return output


data = loadData()
moveTo = int(statistics.median(data))

distance = []
for position in data:
    distance.append(abs(moveTo - position))

total = sum(distance)
print(f"total fuel: {total}")
