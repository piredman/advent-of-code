import csv
from colorama import Fore, Style
fileName = '04/input.txt'


def loadDrawnNumbers():
    output = []
    with open(fileName, 'r', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            if len(row) == 0:
                break

            for column in row:
                output.append(int(column))

    return output


def loadNextGame(lastGameIndex, lastRowIndex):
    isBreak = False
    output = {"lastRow": lastRowIndex, "gameData": []}
    with open(fileName, newline='') as fileData:
        lastRow = output["lastRow"]
        reader = csv.reader(fileData)
        for row in reader:
            if reader.line_num <= lastRow or row == '':
                continue

            if len(row) == 0:
                output["lastRow"] = reader.line_num
                isBreak = True
                break

            splitRow = row[0].split(' ')
            line = []
            for column in splitRow:
                if column.isnumeric():
                    line.append([int(column), False])

            output["gameData"].append(line)

    if not isBreak:
        output["lastRow"] = -1

    return output


def anyRowComplete(gameData):
    match = False
    for columnIndex in list(range(5)):
        marked = 0
        for rowIndex in list(range(5)):
            cell = gameData[columnIndex][rowIndex]
            if cell[1]:
                marked += 1

            if marked == 5:
                match = True
                break

    return match


def anyColumnComplete(gameData):
    match = False
    for columnIndex in list(range(5)):
        marked = 0
        for rowIndex in list(range(5)):
            cell = gameData[rowIndex][columnIndex]
            if cell[1]:
                marked += 1

            if marked == 5:
                match = True
                break

    return match


def processGame(gameNumbers, gameData):
    if len(gameData) <= 0:
        return

    matchFound = False
    finalDraw = 0
    for index, drawnNumber in enumerate(gameNumbers):
        if matchFound:
            break

        for row in gameData:
            if matchFound:
                break

            for column in row:
                if matchFound:
                    break

                if column[0] == drawnNumber:
                    column[1] = True
                    finalDraw = drawnNumber

                    matchFound = anyRowComplete(gameData)
                    if not matchFound:
                        matchFound = anyColumnComplete(gameData)

    return {"cycles": index, "gameData": gameData, "finalDraw": finalDraw}


def printGame(gameData):
    for row in gameData:
        for column in row:
            text = "%2s" % column[0]
            if column[1]:
                print(Fore.GREEN + text, end=" ")
            else:
                print(Fore.WHITE + text, end=" ")
        print()
    print(Fore.WHITE)


def processGames(input):
    gameIndex = 0
    gameNumbers = {"lastRow": 2, "gameData": [0], "cycles": 0}
    bestCycles = 0
    winner = []
    while len(gameNumbers["gameData"]) > 0 and gameNumbers["lastRow"] != -1:
        gameNumbers = loadNextGame(gameIndex, gameNumbers["lastRow"])
        if len(gameNumbers["gameData"]) <= 0:
            break

        gameResult = processGame(input, gameNumbers["gameData"])
        currentCycles = int(gameResult["cycles"])

        if bestCycles == 0:
            bestCycles = currentCycles
            winner = gameNumbers["gameData"]
            finalDraw = gameResult["finalDraw"]
        elif currentCycles > bestCycles:
            bestCycles = currentCycles
            winner = gameNumbers["gameData"]
            finalDraw = gameResult["finalDraw"]

        gameIndex += 1

    return {"winner": winner, "finalDraw": finalDraw}


def sumUnmarkedNumbers(gameData):
    result = 0
    for row in gameData:
        for column in row:
            if not column[1]:
                result += column[0]
    return result


drawnNumbers = loadDrawnNumbers()
result = processGames(drawnNumbers)

print()
print("Winner")

finalDraw = result["finalDraw"]
winner = result["winner"]
printGame(winner)

sum = sumUnmarkedNumbers(winner)
score = sum * finalDraw
print(f"score: {score}")
