import csv
from dataclasses import dataclass
from enum import Enum


class LoadState(Enum):
    STACK = 1
    INSTRUCTIONS = 2


@dataclass
class Stack:
    column: int
    crates: list


@dataclass
class Instruction:
    qty: int
    source: int
    target: int


def load_data():
    stacks: list[Stack] = []
    instructions = []
    load_state = LoadState.STACK

    with open('2022/05/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            if len(row) == 0:
                load_state = LoadState.INSTRUCTIONS
                continue

            if load_state == LoadState.STACK:
                stacks.append([row[0]])
            else:
                instructions.append([row[0]])

    return {'stacks': stacks, 'instructions': instructions}


def create_stacks(input):
    headerValue = input.pop()[0]
    header = list(headerValue)

    stacks: list[Stack] = []
    indexies = []

    for index, value in enumerate(header):
        if value.strip():
            stack = Stack(int(value), [])
            stacks.append(stack)
            indexies.append(index)

    for row in input[::-1]:
        line = list(row[0])
        for index, value in enumerate(indexies):
            crateValue = line[value]
            if crateValue.strip():
                stacks[index].crates.append(crateValue)

    return stacks


def create_instructions(input):
    output: list[Instruction] = []
    for value in input:
        valueList = value[0].split(" ")
        output.append(Instruction(
            int(valueList[1]),
            int(valueList[3]),
            int(valueList[-1]))
        )

    return output


def run_instructions(instructions: list[Instruction], stacks: list[Stack]):
    for instruction in instructions:
        source = stacks[instruction.source - 1]
        target = stacks[instruction.target - 1]

        for index in range(instruction.qty):
            crate = source.crates.pop()
            target.crates.append(crate)

    return stacks


def get_top_crates(input: list[Stack]):
    output = ""
    for stack in input:
        output += stack.crates[-1]

    return output


def print_data(input):
    for row in input['stacks']:
        print(row)

    print()

    for row in input['instructions']:
        print(row)


def print_stacks(input):
    for stack in input:
        print(stack)


def print_instructions(input):
    for instruction in input:
        print(instruction)


data = load_data()
# print_data(data)

stacks = create_stacks(data['stacks'])
print_stacks(stacks)

instructions = create_instructions(data['instructions'])
print_instructions(instructions)

updatedStacks = run_instructions(instructions, stacks)
print_stacks(updatedStacks)

print(get_top_crates(updatedStacks))
