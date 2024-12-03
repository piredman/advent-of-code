import csv

words = "one two three four five six seven eight nine".split()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def loadData():
    input = []
    with open("2023/01/sample2.txt", newline="") as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            line = row[0]
            print(line)
            value = findFirst(line)
            input.append(line)

    return input


def findFirst(line=""):
    foundIndex = len(line)
    for idx, word in enumerate(words):
        # number = numbers[idx]
        value = line.find(word, 0)
        if value > -1 and value < foundIndex:
            print(f"word: {word}, index: {foundIndex}")
            foundIndex = value
            break

    return foundIndex


def find_occurances(input, word):
    return []


data = loadData()
print(data)
