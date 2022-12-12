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
class Signal:
    cycle: int
    register: int

    def get_strength(self):
        return self.cycle * self.register

    def __str__(self):
        return f'cycle: {self.cycle}, register: {self.register}, strength: {self.get_strength()}'


@dataclass
class CPU:
    cycle: int = 0
    register: int = 1
    signals: list[Signal] = field(default_factory=list[Signal])

    def __str__(self):
        return f'[CPU] cycle: {self.cycle}, register: {self.register}, signals: {len(self.signals)}'


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
            cpu.cycle += 1
            if (cpu.cycle == 20) or ((cpu.cycle - 20) % 40 == 0):
                cpu.signals.append(Signal(cpu.cycle, cpu.register))

        if instruction.command == Command.ADDX:
            cpu.register += instruction.arg

    return cpu


program = load_data()
print('PROGRAM')
[print(line) for line in program]
print()

cpu = run(CPU(), program)
print(cpu)
[print(line) for line in cpu.signals]

print(sum(list(map(lambda signal: signal.get_strength(), cpu.signals))))
