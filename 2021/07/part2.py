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
moveTo = int(statistics.mean(data))

fuel = []
for position in data:
    distance = abs(position - moveTo)
    cost = distance * (distance + 1) / 2
    fuel.append(int(cost))

totalFuel = sum(fuel)
print(f"total fuel: {totalFuel}")
