import csv


def load_data():
    input = []
    with open('2022/04/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            input.append([row[0], row[1]])

    return input


def convert_data(input):
    output = []
    for row in input:
        line = []
        for column in row:
            line.append(convert_numbers(column))
        output.append(line)

    return output


def convert_numbers(input):
    values = input.split('-')
    start = int(values[0])
    stop = int(values[1])

    output = []
    for value in range(start, stop + 1):
        output.append(value)

    return output


def within(a, b):
    aInB = any(element in b for element in a)
    bInA = any(element in a for element in b)
    return aInB or bInA


def print_data(input):
    for row in input:
        print(row)


data = load_data()
converted = convert_data(data)

total = 0
for line in converted:
    if within(line[0], line[1]):
        total += 1


print(total)
