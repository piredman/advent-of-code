import csv
from collections import Counter

PRIORITIES = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def load_data():
    input = []
    group = []
    with open('2022/03/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for index, row in enumerate(reader):
            group.append(row[0])
            if (index + 1) % 3 == 0:
                input.append(group)
                group = []

    return input


def compare_strings(a, b):
    output = []
    if a is None or b is None:
        return output

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                output.append(a[i])

    return ''.join(set(output))


def convert_to_priorities(input):
    return PRIORITIES.index(input) + 1


def print_data(input):
    for row in input:
        print(row)


total = 0
data = load_data()
for group in data:
    common = compare_strings(group[0], group[1])
    common = compare_strings(common, group[2])
    priority = convert_to_priorities(common)
    total += priority

print(total)
