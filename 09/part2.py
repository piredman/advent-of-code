import csv
import math
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
    items = [i for i in neighbours if i != None]
    for neighbour in items:
        if neighbour <= current:
            return False

    return True


def getNeighbours(input, row, column, rows, columns):
    neighbours = []

    cell = row - 1
    if cell >= 0 and cell < rows:
        neighbours.append(input[cell][column])
    else:
        neighbours.append(None)

    cell = column + 1
    if cell >= 0 and cell < columns:
        neighbours.append(input[row][cell])
    else:
        neighbours.append(None)

    cell = row + 1
    if cell >= 0 and cell < rows:
        neighbours.append(input[cell][column])
    else:
        neighbours.append(None)

    cell = column - 1
    if cell >= 0 and cell < columns:
        neighbours.append(input[row][cell])
    else:
        neighbours.append(None)

    return neighbours


def cellInBounds(cell, rows, columns):
    if cell[0] >= 0 and cell[0] < rows and cell[1] >= 0 and cell[1] < columns:
        return True

    return False


def processCell(input, cell, rows, columns):
    if cellInBounds(cell, rows, columns):
        value = input[cell[0]][cell[1]]
        if value[0] < 9 and value[1] == 0:
            value[1] = 2
            return cell

    return None


def processRing(input, row, column, rows, columns):
    count = 0
    cells = [[row-1, column],  # up
             [row, column+1],  # right
             [row+1, column],  # down
             [row, column-1]]  # left

    for cell in cells:
        newCell = processCell(input, cell, rows, columns)
        if newCell:
            count += 1
            count += processRing(input, cell[0], cell[1], rows, columns)

    return count


def processBasin(input, row, column, rows, columns):
    count = processRing(input, row, column, rows, columns)
    return count + 1


def processBasins(input):
    output = []
    rows = len(input)
    columns = len(input[0])
    for column in list(range(columns)):
        for row in list(range(rows)):
            cell = input[row][column]
            if cell[1] == 1:
                count = processBasin(input, row, column, rows, columns)
                output.append(count)

    return output


def getLowPoints(input):
    rows = len(input)
    columns = len(input[0])
    output = []

    for column in list(range(columns)):
        line = []
        for row in list(range(rows)):
            neighbours = getNeighbours(
                input, row, column, rows, columns)
            current = input[row][column]
            isLowest = isLowerThanNeighbours(current, neighbours)
            line.append([current, 1 if isLowest else 0])

        output.append(line)

    return output


def drawByColumn(input):
    print()
    rows = len(input)
    columns = len(input[0])
    for column in list(range(columns)):
        for row in list(range(rows)):
            cell = input[row][column]
            if cell[1] == 2:
                print(Fore.BLUE + str(cell[0]), end=" ")
            elif cell[1] == 1:
                print(Fore.GREEN + str(cell[0]), end=" ")
            else:
                print(Fore.WHITE + str(cell[0]), end=" ")
        print(Fore.WHITE)
    print(Fore.WHITE)


data = loadData()
lowPoints = getLowPoints(data)
basins = processBasins(lowPoints)
drawByColumn(lowPoints)
sortedList = sorted(basins)
lastThree = sortedList[-3:]
total = math.prod(lastThree)
print(f"total: {total}")
