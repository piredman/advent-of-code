import csv
from colorama import Fore
fileName = '09/input.txt'


def loadData():
    output = []
    with open(fileName, 'r', newline='') as fileData:
        reader = csv.reader(fileData, delimiter='|')
        for row in reader:
            for column in row:
                output.append([int(i) for i in list(column)])

    return output


def isLowerThanNeighbours(current, neighbours):
    for neighbour in neighbours:
        if neighbour <= current:
            return False

    return True


def processNeighbours(input):
    rows = len(input)
    columns = len(input[0])
    output = []
    lowest = []

    for column in list(range(columns)):
        line = []
        for row in list(range(rows)):
            neighbours = []

            cell = row - 1
            if cell >= 0 and cell < rows:
                neighbours.append(input[cell][column])

            cell = column + 1
            if cell >= 0 and cell < columns:
                neighbours.append(input[row][cell])

            cell = row + 1
            if cell >= 0 and cell < rows:
                neighbours.append(input[cell][column])

            cell = column - 1
            if cell >= 0 and cell < columns:
                neighbours.append(input[row][cell])

            current = input[row][column]
            isLowest = isLowerThanNeighbours(current, neighbours)
            line.append([current, isLowest])
            if isLowest:
                lowest.append(current + 1)

        output.append(line)

    return [output, lowest]


def drawByColumn(input):
    print()
    rows = len(input)
    columns = len(input[0])
    for column in list(range(columns)):
        for row in list(range(rows)):
            cell = input[row][column]
            if cell[1]:
                print(Fore.GREEN + str(cell[0]), end=" ")
            else:
                print(Fore.WHITE + str(cell[0]), end=" ")
        print()
    print(Fore.WHITE)


data = loadData()
final = processNeighbours(data)
drawByColumn(final[0])
lowest = final[1]
print(f"Risk: {sum(lowest)}")
