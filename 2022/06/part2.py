import csv
from dataclasses import dataclass
from enum import Enum


def load_data():
    output: list = []
    with open('2022/06/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            output.append(row[0])

    return output


def process(input: list):
    output: list = []
    for item in input:
        output.append(get_start_of_message_marker(item))

    return output


def get_start_of_message_marker(input: str):
    output = {
        'index': 0,
        'marker': ''
    }

    size = len(input)
    for index in range(size):
        end = index + 14
        if end > size:
            break

        marker = input[index:end]
        if not are_different(marker):
            output['index'] = end
            output['marker'] = marker
            break

    return output


def are_different(input: str):
    characters = list(input)
    count = len(characters)

    duplicates = False
    for i in range(count):
        first = characters[i]
        for j in range(count):
            if i == j:
                continue

            second = characters[j]
            if first == second:
                duplicates = True
                break

    return duplicates


def print_markers(input: list):
    for item in input:
        print(item)


data = load_data()
print(data)

markers = process(data)
print_markers(markers)
