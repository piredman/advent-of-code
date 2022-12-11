import csv
from dataclasses import dataclass, field
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

    @staticmethod
    def add(one, two):
        return Position(one.row + two.row, one.col + two.col)


@dataclass
class Positions:
    start: Position = Position(0, 0)
    head: Position = start
    knots: list[Position] = field(default_factory=list)
    tail_positions: list[Position] = field(default_factory=list)

    def __str__(self):
        knots = '['
        for knot in self.knots:
            knots += f'{knot}'
        knots += ']'

        return f'start: {self.start}, head: {self.head}, knots: {knots}, tail_positions: {len(self.tail_positions)}'


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
    positions.tail_positions.append(positions.head)
    for instruction in instructions:
        execute(instruction, positions)
        # print(positions)
        # print_as_grid(positions)
        # print()


def execute(instruction: Instruction, positions: Positions):
    print(instruction)
    for step in range(instruction.distance):
        positions.head = move(instruction.direction, positions.head)
        head = positions.head
        for index, knot in enumerate(positions.knots):
            head = follow(head, knot)
            positions.knots[index] = head

        track_tail_position(positions.tail_positions, head)

        # print(positions)
        # print_as_grid(positions)
        # print()

    print()


def track_tail_position(tail_positions: list[Position], tail: Position):
    if tail not in tail_positions:
        tail_positions.append(tail)


def follow(head: Positions, tail: Position):
    difference = Position(
        (head.row - tail.row),
        (head.col - tail.col)
    )

    if (difference.col > 1):
        tail = move(Direction.RIGHT, tail)
        if (difference.row > 0):
            tail = move(Direction.UP, tail)
        elif (difference.row < 0):
            tail = move(Direction.DOWN, tail)

    elif (difference.col < -1):
        tail = move(Direction.LEFT, tail)
        if (difference.row > 0):
            tail = move(Direction.UP, tail)
        elif (difference.row < 0):
            tail = move(Direction.DOWN, tail)

    elif (difference.row > 1):
        tail = move(Direction.UP, tail)
        if (difference.col > 0):
            tail = move(Direction.RIGHT, tail)
        elif (difference.col < 0):
            tail = move(Direction.LEFT, tail)

    elif (difference.row < -1):
        tail = move(Direction.DOWN, tail)
        if (difference.col > 0):
            tail = move(Direction.RIGHT, tail)
        elif (difference.col < 0):
            tail = move(Direction.LEFT, tail)

    return tail


def move(direction: Direction, position: Position):
    move = {
        Direction.UP: lambda pos: Position(pos.row + 1, pos.col),
        Direction.DOWN: lambda pos: Position(pos.row - 1, pos.col),
        Direction.RIGHT: lambda pos: Position(pos.row, pos.col + 1),
        Direction.LEFT: lambda pos: Position(pos.row, pos.col - 1)
    }
    return move.get(direction)(position)


def print_as_grid(pos: Positions):
    offset = Position(6, 12)
    # offset = Position(0, 0)
    head = Position.add(pos.head, offset)

    row_max = 21  # max(pos.start.row, pos.head.row, pos.tail.row)
    col_max = 26  # max(pos.start.col, pos.head.col, pos.tail.col)
    # row_max = 4  # max(pos.start.row, pos.head.row, pos.tail.row)
    # col_max = 5  # max(pos.start.col, pos.head.col, pos.tail.col)

    rows = []
    for row in range(row_max + 1):
        column = []
        for col in range(col_max + 1):

            current = Position(row, col)
            if current == head:
                column.append('H')
                continue

            found = False
            for index, knot in enumerate(pos.knots):
                if current == Position.add(knot, offset):
                    column.append(index + 1)
                    found = True
                    break
            if found:
                continue

            if current == Position.add(pos.start, offset):
                column.append('s')
                continue

            column.append('.')

        rows.append(column)

    for row in rows[::-1]:
        for col in row:
            print(col, end='')
        print()


instructions = load_data()
positions = Positions()
for knot in range(9):
    positions.knots.append(positions.head)

print('BEGIN')
print(positions)
print()

tail_positions = run(instructions, positions)

print('END')
print(positions)
