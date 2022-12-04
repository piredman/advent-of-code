import csv
from colorama import Fore
fileName = '11/input.txt'
data = []
rows = 0
columns = 0


def loadData():
    output = []
    with open(fileName, 'r', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            for column in row:
                line = []
                for cell in list(column):
                    line.append(int(cell))
                output.append(line)

    return output


def cellInBounds(row, column):
    if row >= 0 and row < rows and column >= 0 and column < columns:
        return True

    return False


def processFlashes(flashes):
    newFlashes = []
    for flash in flashes:
        row = flash[0]
        col = flash[1]
        if data[row][col] == 0:
            newFlashes += processNeighbours(row, col)

    return newFlashes


def processNeighbours(row, column):
    newFlashes = []
    neighbours = [[row-1, column],  # up
                  [row-1, column+1],  # up,right
                  [row, column+1],  # right
                  [row+1, column+1],  # down,right
                  [row+1, column],  # down
                  [row+1, column-1],  # down,left
                  [row, column-1],  # left
                  [row-1, column-1]]  # up,left

    for neighbour in neighbours:
        nRow = neighbour[0]
        nCol = neighbour[1]
        if cellInBounds(nRow, nCol):
            if data[nRow][nCol] != 0:
                data[nRow][nCol] += 1
                if data[nRow][nCol] > 9:
                    data[nRow][nCol] = 0
                    newFlashes.append([nRow, nCol])

    return newFlashes


def countNonZeros():
    count = 0
    for row in list(range(rows)):
        for column in list(range(columns)):
            cell = data[row][column]
            if cell != 0:
                count += 1

    return count


def process():
    flashes = []
    for row in list(range(rows)):
        for column in list(range(columns)):
            data[row][column] += 1
            if data[row][column] > 9:
                data[row][column] = 0
                flashes.append([row, column])

    count = len(flashes)
    newFlashes = processFlashes(flashes)
    while len(newFlashes) > 0:
        count += len(newFlashes)
        newFlashes = processFlashes(newFlashes)

    return count


def draw():
    print()
    for row in list(range(rows)):
        for column in list(range(columns)):
            cell = data[row][column]
            value = cell
            if value == 0:
                print(Fore.WHITE + str(value), end=" ")
            else:
                print(Fore.GREEN + str(value), end=" ")
        print(Fore.WHITE)
    print(Fore.WHITE)


data = loadData()
rows = len(data)
columns = len(data[0])

print()
print(f"Before any steps:")
draw()

step = 0
count = countNonZeros()
while count > 0:
    step += 1
    process()
    count = countNonZeros()

print(f"After step {step + 1}:")
draw()
print(f"simultneous flash on step {step}")
