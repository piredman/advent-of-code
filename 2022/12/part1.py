import csv
from dataclasses import dataclass, field
from enum import Enum, auto

start = (0, 0)
end = (0, 0)
neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]
elevation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def load_data() -> list:
    global start, end
    output: list = []
    with open('2022/12/sample.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row_index, row in enumerate(reader):
            line = []
            for col_index, col in enumerate(row[0]):
                if col == 'S':
                    start = (row_index, col_index)
                if col == 'E':
                    end = (row_index, col_index)

                line.append(col)
            output.append(line)

    return output


def run(data):
    global location, start, end

    print_location(start, data)
    print_location(end, data)


def print_location(coord, grid):
    print(f'{coord} {grid[coord[0]][coord[1]]}')


def print_grid(data):
    for row in data:
        for col in row:
            print(col, end="")
        print()


data = load_data()
print_grid(data)

run(data)
