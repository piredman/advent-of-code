import csv
fileName = '08/input.txt'


def loadData():
    output = []
    with open(fileName, 'r', newline='') as fileData:
        reader = csv.reader(fileData, delimiter='|')
        for row in reader:
            line = []
            for column in row:
                line.append(list(filter(None, column.split(' '))))
            output.append(line)

    return output


data = loadData()

count = 0
for line in data:
    for item in line[1]:
        length = len(item)
        if length == 2 or length == 3 or length == 4 or length == 7:
            count += 1

print(f"1, 4, 7, or 8 appear {count} times")
