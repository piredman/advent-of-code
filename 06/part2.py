import csv
import functools
fileName = '06/input.txt'
days = 256
school = []


def loadData(file):
    output = []
    with open(file, 'r', newline='') as fileData:
        reader = csv.reader(fileData, delimiter=',')
        row = next(reader)
        output = [int(x) for x in row]

    return output


school = loadData(fileName)
counts = [0]*9
for fish in school:
    counts[fish] += 1

for day in list(range(days)):
    fishAtZero = counts[0]
    for index, age in enumerate(counts):
        if (index + 1) >= len(counts):
            break
        counts[index] = counts[index + 1]

    counts[8] = fishAtZero
    counts[6] += fishAtZero

sum = functools.reduce(lambda a, b: a + b, counts)
print(f"There are {sum} fish in the school after {days} days")
