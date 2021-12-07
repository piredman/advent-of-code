import csv
from os import getpgid
from colorama import Fore
fileName = '05/input.txt'
gridSize = 1000


def loadData():
    output = []
    with open(fileName, 'r', newline='') as fileData:
        reader = csv.reader(fileData, delimiter=' ')
        for row in reader:
            xPoint = [int(x) for x in row[0].split(',')]
            yPoint = [int(x) for x in row[2].split(',')]
            output.append([xPoint, yPoint])

    return output


def dropVertical(input):
    output = []
    for row in input:
        if row[0][0] == row[1][0] or row[0][1] == row[1][1]:
            output.append(row)

    return output


def generateArea():
    area = []
    for rowIndex in list(range(gridSize)):
        line = []
        for columnIndex in list(range(gridSize)):
            line.append(0)
        area.append(line)

    return area


def getPoints(lines, area):
    points = []
    for line in lines:
        start = line[0]
        end = line[1]

        x1 = start[0]
        y1 = start[1]
        x2 = end[0]
        y2 = end[1]

        if x1 == x2:
            first = min(y1, y2)
            last = max(y1, y2)
            for y in range(first, last + 1):
                points.append([x1, y])

            # print(temp)
            continue

        if y1 == y2:
            first = min(x1, x2)
            last = max(x1, x2)
            for x in range(first, last + 1):
                points.append([x, y1])

            # print(temp)
            continue

        count = abs(x1 - x2)
        xChange = 1 if x1 < x2 else -1
        yChange = 1 if y1 < y2 else -1

        x = x1
        y = y1
        points.append([x, y])
        for index in list(range(count)):
            x += xChange
            y += yChange
            points.append([x, y])

    return points


def updateArea(points, area):
    for point in points:
        area[point[1]][point[0]] += 1


def getOverlap(area):
    output = 0
    for row in area:
        for column in row:
            if column >= 2:
                output += 1
    return output


def draw(input):
    for row in input:
        for column in row:
            if column == 0:
                print(Fore.WHITE + ".", end=" ")
            else:
                print(Fore.WHITE + str(column), end=" ")
        print()
    print()


data = loadData()
area = generateArea()
points = getPoints(data, area)
updateArea(points, area)
overlap = getOverlap(area)
draw(area)
print(f"number of overlaping lines: {overlap}")
