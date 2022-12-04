import csv
from os import linesep
from colorama import Fore
fileName = '10/input.txt'

chunks = [['(', ')', 3], ['[', ']', 57], ['{', '}', 1197], ['<', '>', 25137]]


def loadData():
    output = []
    with open(fileName, 'r', newline='') as fileData:
        reader = csv.reader(fileData, delimiter='|')
        for row in reader:
            for column in row:
                output.append(list(column))

    return output


def countCharacter(line, character):
    count = 0
    for item in line:
        if item == character:
            count += 1
    return count


def getOpening(character):
    for chunk in chunks:
        if character == chunk[0]:
            return chunk
    return None


def reviewLine(line):
    output = None
    lineStack = []
    for character in line:
        opening = getOpening(character)
        if opening:
            lineStack.append(opening[1])
            continue

        closing = lineStack[-1]
        if closing == character:
            lineStack.pop()
            continue

        print(f"Expected {closing} but found {character}")
        output = character
        break

    if not output:
        print(f"incomplete line, ignoring...")

    return output


def calculateScore(endings):
    scores = []
    for ending in endings:
        for chunk in chunks:
            if ending == chunk[1]:
                scores.append(chunk[2])
                print(f"{ending}: {chunk[2]} points.")
                break

    return sum(scores)


illegalEndings = []
rawData = loadData()
for line in rawData:
    result = reviewLine(line)
    if result:
        illegalEndings.append(result)

print()
score = calculateScore(illegalEndings)
print(f"score: {score}")
