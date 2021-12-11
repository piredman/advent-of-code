import csv
from os import linesep
from colorama import Fore
fileName = '10/input.txt'

chunks = [['(', ')', 1], ['[', ']', 2], ['{', '}', 3], ['<', '>', 4]]


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

        print(f"corrupted line, ignoring...")
        output = character
        break

    if not output:
        lineStack.reverse()
        print(f"completed by adding {''.join(lineStack)}")
        return lineStack

    return []


def calculateScore(endings):
    print()
    scores = []
    for ending in endings:
        score = 0
        for character in ending:
            score = score * 5
            for chunk in chunks:
                if character == chunk[1]:
                    score += chunk[2]
                    break

        print(f"{''.join(ending)} - {score} total points")
        scores.append(score)

    scores.sort()
    index = int((len(scores) - 1) / 2)
    return scores[index]


endings = []
rawData = loadData()
for line in rawData:
    result = reviewLine(line)
    if result:
        endings.append(result)

print()
score = calculateScore(endings)
print(f"score: {score}")
