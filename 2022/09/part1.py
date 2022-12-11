import csv
from dataclasses import dataclass
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    UP_RIGHT = auto()
    RIGHT = auto()
    DOWN_RIGHT = auto()
    DOWN = auto()
    DOWN_LEFT = auto()
    LEFT = auto()
    UP_LEFT = auto()


@dataclass
class Instruction:
    direction: Direction
    distance: int

    def __str__(self):
        return f'move {self.distance} {self.direction.name}'


@dataclass
class Position:
    row: int
    col: int

    def __str__(self):
        return f'({self.row}, {self.col})'


@dataclass
class Positions:
    start: Position = Position(0, 0)
    head: Position = start
    tail: Position = head

    def __str__(self):
        return f'start: {self.start}, head: {self.head}, tail: {self.tail}'


def load_data():
    output: list = []
    with open('2022/09/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            line = row[0].split(' ')
            direction = direction_from_string(line[0])
            output.append(Instruction(direction, int(line[1])))

    return output


def direction_from_string(input: str):
    switcher = {
        'U': Direction.UP,
        'D': Direction.DOWN,
        'L': Direction.LEFT,
        'R': Direction.RIGHT
    }
    return switcher.get(input)


def print_data(data):
    print('Instructions')
    for line in data:
        print(line)
    print()


def run(instructions: list[Instruction], positions: Positions):
    tail_positions: list[Position] = []
    tail_positions.append(positions.tail)
    for instruction in instructions:
        tail_positions = execute(instruction, positions, tail_positions)

    return tail_positions


def execute(instruction: Instruction, positions: Positions, tail_positions: list[Position]):
    print(instruction)
    for step in range(instruction.distance):
        positions.head = move(instruction.direction, positions.head)
        tail_positions = follow(positions, tail_positions)
        # print(positions)
        # print_as_grid(positions)
        # print()

    print()
    return tail_positions


def follow(positions: Positions, tail_positions: list[Position]):
    difference = Position(
        (positions.head.row - positions.tail.row),
        (positions.head.col - positions.tail.col)
    )

    if (difference.col > 1):
        positions.tail = positions.tail = move(Direction.RIGHT, positions.tail)
        if (abs(difference.row) > 0):
            positions.tail.row = positions.head.row
        track_tail_position(tail_positions, positions.tail)
    elif (difference.col < -1):
        positions.tail = positions.tail = move(Direction.LEFT, positions.tail)
        if (abs(difference.row) > 0):
            positions.tail.row = positions.head.row
        track_tail_position(tail_positions, positions.tail)
    elif (difference.row > 1):
        positions.tail = positions.tail = move(Direction.UP, positions.tail)
        if (abs(difference.col) > 0):
            positions.tail.col = positions.head.col
        track_tail_position(tail_positions, positions.tail)
    elif (difference.row < -1):
        positions.tail = positions.tail = move(Direction.DOWN, positions.tail)
        if (abs(difference.col) > 0):
            positions.tail.col = positions.head.col
        track_tail_position(tail_positions, positions.tail)

    return tail_positions


def track_tail_position(tail_positions: list[Position], tail: Position):
    if tail not in tail_positions:
        tail_positions.append(tail)


def move(direction: Direction, position: Position):
    move = {
        Direction.UP: lambda pos: Position(pos.row + 1, pos.col),
        Direction.DOWN: lambda pos: Position(pos.row - 1, pos.col),
        Direction.RIGHT: lambda pos: Position(pos.row, pos.col + 1),
        Direction.LEFT: lambda pos: Position(pos.row, pos.col - 1)
    }
    return move.get(direction)(position)


def print_as_grid(pos: Positions):
    row_max = max(pos.start.row, pos.head.row, pos.tail.row)
    col_max = max(pos.start.col, pos.head.col, pos.tail.col)

    rows = []
    for row in range(row_max + 1):
        column = []
        for col in range(col_max + 1):
            current = Position(row, col)
            if current == pos.head:
                column.append('H')
            elif current == pos.tail:
                column.append('T')
            elif current == pos.start:
                column.append('s')
            else:
                column.append('.')
        rows.append(column)

    for row in rows[::-1]:
        for col in row:
            print(col, end='')
        print()


instructions = load_data()
positions = Positions()
print('BEGIN')
print(positions)
print()

tail_positions = run(instructions, positions)

print('END')
print(positions)
print(f'tail visited: {len(tail_positions)}')
print()
