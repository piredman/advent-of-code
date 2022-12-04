import csv
import array

def loadData():
    numberData = array.array('d', [])
    with open('input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            numberData.append(int(row[0]))

    return numberData

def processNumbers(numbers):
    increases = 0
    previous = 0
    for current in numbers:
        increases += processNumber(previous, current)
        previous = current

    return increases

def processNumber(previous, current):
    if (previous == 0):
        print(str(current) + ' (N/A - no previous measurement)')
        return 0

    if current < previous:
        print(str(current) + ' (Decrease)')
        return 0

    if current == previous:
        print(str(current) + ' (Same)')
        return 0

    print(str(current) + ' (Increase)')
    return 1

data = loadData()
result = processNumbers(data)
print(result)