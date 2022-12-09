import csv
from dataclasses import dataclass
from colorama import Fore
from enum import Enum


@dataclass
class Tree:
    height: int
    visible: True


@dataclass
class Coordinate:
    row: int
    col: int


@dataclass
class Grid:
    min: Coordinate
    max: Coordinate


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def load_data():
    output: list = []
    with open('2022/08/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for x, row in enumerate(reader):
            line: list[Tree] = []
            for y, column in enumerate(row[0]):
                line.append(Tree(int(column[0]), True))
            output.append(line)

    return output


def process(input: list):
    tree_grid = Grid(
        Coordinate(0, 0),
        Coordinate(len(input) - 1, len(input[0]) - 1)
    )

    for row_index in range(tree_grid.min.row, tree_grid.max.row + 1):
        for col_index in range(tree_grid.min.col, tree_grid.max.col + 1):
            determine_visible(input, tree_grid,
                              Coordinate(row_index, col_index))


def determine_visible(trees, grid: Grid, cords: Coordinate):
    tree = trees[cords.row][cords.col]
    if cords.row == grid.min.row or cords.row == grid.max.row or \
       cords.col == grid.min.col or cords.col == grid.max.col:
        return

    up = True
    down = True
    left = True
    right = True

    for direction in Direction:

        if direction == Direction.UP:
            row = cords.row - 1
            while row >= grid.min.row:
                neighbour = trees[row][cords.col].height
                if tree.height <= neighbour:
                    up = False
                    break
                row -= 1

        if direction == Direction.DOWN:
            row = cords.row + 1
            while row <= grid.max.row:
                neighbour = trees[row][cords.col].height
                if tree.height <= neighbour:
                    down = False
                    break
                row += 1

        if direction == Direction.LEFT:
            col = cords.col - 1
            while col >= grid.min.col:
                neighbour = trees[cords.row][col].height
                if tree.height <= neighbour:
                    left = False
                    break
                col -= 1

        if direction == Direction.RIGHT:
            col = cords.col + 1
            while col <= grid.max.col:
                neighbour = trees[cords.row][col].height
                if tree.height <= neighbour:
                    right = False
                    break
                col += 1

    if not up and not down and not left and not right:
        tree.visible = False


def get_counts(trees):
    visble = 0
    hidden = 0

    for row in trees:
        for col in row:
            if col.visible:
                visble += 1
            else:
                hidden += 1

    return [visble, hidden]


def print_data(input: list):
    for line in input:
        for tree in line:
            if tree.visible:
                print(Fore.WHITE + str(tree.height), end=" ")
            else:
                print(Fore.GREEN + str(tree.height), end=" ")
        print(Fore.WHITE)


data = load_data()
rows = len(data)
columns = len(data[0])

total_trees = rows * columns
inner_trees = (rows - 2) * (columns - 2)
outer_trees = total_trees - inner_trees

print(f'total: {total_trees}, inner: {inner_trees}, outer: {outer_trees}')

process(data)
print_data(data)

counts = get_counts(data)
print(f'visible: {counts[0]}, hidden: {counts[1]}')
