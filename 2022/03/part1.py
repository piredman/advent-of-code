import csv
from collections import Counter

PRIORITIES = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def load_data():
    input = []
    with open('2022/03/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            item = row[0]
            size = len(item)
            input.append([item[0:size//2], item[size//2:]])

    return input


def compare_strings(strings):
    output = []
    a = strings[0]
    b = strings[1]

    if a is None or b is None:
        return output

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                output.append(a[i])

    return set(output).pop()


def convert_to_priorities(input):
    return PRIORITIES.index(input) + 1


def print_data(input):
    for row in input:
        print(row)


data = load_data()

total = 0
for line in data:
    total += convert_to_priorities(compare_strings(line))

print(total)
