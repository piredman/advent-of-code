import csv
from dataclasses import dataclass, field
from enum import Enum, auto


class Command(Enum):
    NOOP = auto()
    ADDX = auto()


@dataclass
class Instruction:
    command: Command
    arg: int

    def __str__(self):
        cmd = self.command.name.lower()
        cycle = self.command.value
        output = cmd if not self.arg else f'{cmd} {self.arg}'
        return f'[{cycle}] {output}'


@dataclass
class CPU:
    cycle: int = 0
    register: int = 1

    def __str__(self):
        return f'[CPU] cycle: {self.cycle}, register: {self.register}'


def load_data() -> list[str]:
    output: list[str] = []
    with open('2022/10/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            line = row[0].split(' ')
            cmd = command_from_string(line[0])
            instruction = Instruction(cmd, None) if len(
                line) <= 1 else Instruction(cmd, int(line[1]))
            output.append(instruction)

    return output


def command_from_string(input: str) -> Command:
    switcher = {
        'addx': Command.ADDX,
        'noop': Command.NOOP
    }
    return switcher.get(input)


def run(cpu: CPU, program: list[Instruction]):
    while len(program) > 0:
        instruction = program.pop(0)
        for cycle in range(instruction.command.value):
            if (cpu.cycle % 40) in [cpu.register - 1, cpu.register, cpu.register + 1]:
                print('#', end="")
            else:
                print('.', end="")

            cpu.cycle += 1
            if (cpu.cycle % 40 == 0):
                print()

        if instruction.command == Command.ADDX:
            cpu.register += instruction.arg

    return cpu


program = load_data()
cpu = run(CPU(), program)
print(cpu)
