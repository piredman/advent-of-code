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
    for index, numberValue in enumerate(numbers):
        current = getThree(index, numbers)
        if current >= 0:
            increases += processNumber(previous, current)
            previous = current
    
    return increases

def processNumber(previous, current):
    if (previous == 0):
        print(str(current) + ' (N/A - no previous sum)')
        return 0

    if current < previous:
        print(str(current) + ' (Decrease)')
        return 0

    if current == previous:
        print(str(current) + ' (no change)')
        return 0

    print(str(current) + ' (Increase)')
    return 1

def getThree(start, numbers):
    threeNumbers = numbers[start:start+3]
    if len(threeNumbers) != 3:
        return -1

    print(threeNumbers)
    return sum(x for x in threeNumbers)

data = loadData()
result = processNumbers(data)
print(result)