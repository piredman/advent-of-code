import csv
from dataclasses import dataclass, field
from enum import Enum, auto


class Action(Enum):
    NONE = auto()
    ADD = auto()
    MULTIPLY = auto()

    def __str__(self) -> str:
        if self.name == 'ADD':
            return '+'

        if self.name == 'MULTIPLY':
            return '*'

        return super().__str__()


class ActionOn(Enum):
    SELF = auto()
    AMOUNT = auto()


@dataclass
class Operation:
    action: Action = Action.NONE
    action_on: ActionOn = ActionOn.AMOUNT
    amount: int = 0


@dataclass
class Test:
    divisible_by: int = 0
    throw_to_true: int = 0
    throw_to_false: int = 0


@dataclass
class Monkey:
    id: int = 0
    items: list[int] = field(default_factory=list[int])
    operation: Operation = Operation()
    test: Test = Test()
    inspected: int = 0

    def __str__(self) -> str:
        line = f'Monkey {self.id} \n'
        line += f'  Starting items: {",".join(map(str, self.items))} \n'

        action = self.operation.action
        value = str(self.operation.amount) \
            if self.operation.action_on == ActionOn.AMOUNT \
            else 'old'
        line += f'  Operation: new = old {action} {value} \n'

        line += f'  Test: divisible by {self.test.divisible_by} \n'
        line += f'    If true: throw to monky {self.test.throw_to_true} \n'
        line += f'    If false: throw to monky {self.test.throw_to_false}'
        return line

    def print_items(self):
        print(f'Monkey {Monkey.id}:', end=' ')
        for item in self.items:
            print(item, end=', ')


def load_data() -> list[Monkey]:
    output: list[Monkey] = []
    with open('2022/11/input.txt', newline='') as fileData:
        reader = csv.reader(fileData, delimiter=':')
        for line in reader:
            if len(line) == 0:
                output.append(monkey)
                continue

            header = line[0].strip().lower()
            arg = line[1].strip()

            if header.startswith('monkey'):
                monkey = Monkey(id=len(output))

            monkey = load_line(header, arg, monkey)

        if monkey:
            output.append(monkey)

    return output


def load_line(header: str, arg: str, monkey: Monkey) -> Monkey:
    switcher = {
        'starting items': load_starting_items,
        'operation': load_operation,
        'test': load_test
    }
    func = switcher.get(header, None)
    if func:
        return func(arg, monkey)

    if header == 'if true':
        return load_test_result(True, arg, monkey)

    if header == 'if false':
        return load_test_result(False, arg, monkey)

    return monkey


def load_starting_items(arg: str, monkey: Monkey) -> Monkey:
    for item in arg.split(','):
        monkey.items.append(int(item.strip()))

    return monkey


def load_operation(arg: str, monkey: Monkey) -> Monkey:
    operation_array = arg.split(' ')

    switcher = {
        '*': Action.MULTIPLY,
        '+': Action.ADD
    }
    action = switcher.get(operation_array[3])

    if operation_array[4] == 'old':
        action_on = ActionOn.SELF
        amount = 0
    else:
        action_on = ActionOn.AMOUNT
        amount = int(operation_array[4])

    monkey.operation = Operation(action, action_on, amount)
    return monkey


def load_test(arg: str, monkey: Monkey) -> Monkey:
    test_array = arg.split(' ')
    monkey.test = Test(int(test_array[2]))
    return monkey


def load_test_result(test_result: bool, arg: str, monkey: Monkey) -> Monkey:
    result_array = arg.split(' ')
    id = int(result_array[3])

    if test_result:
        monkey.test.throw_to_true = id
    else:
        monkey.test.throw_to_false = id
    return monkey


def run(monkeys: list[Monkey], rounds: int, print_output: bool):
    for round in range(rounds):
        for monkey in monkeys:
            if print_output:
                print(f'Monkey {monkey.id}')

            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                if print_output:
                    print(
                        f'  Monkey inspects an item with a worry level of {item}.')

                item = execute_operation(item, monkey)
                if print_output:
                    print(f'    Worry level is {item}.')

                item = item // 3
                if print_output:
                    print(
                        f'    Monkey gets bored with item. Worry level is {item}.')

                is_divisible, divisible_by = execute_divisible(item, monkey)
                text = 'is' if is_divisible else 'is not'
                if print_output:
                    print(
                        f'    Current worry level {text} divisible by {divisible_by}.')

                id = get_throw_to(is_divisible, monkey)
                throw_to(id, item, monkeys)
                if print_output:
                    print(
                        f'    Item with worry level {item} is thrown to monkey {id}.')

                monkey.inspected += 1

        #print(f'Round {round + 1}')
        # print_monkey_items(monkeys)
        # print()


def execute_operation(item: int, monkey: Monkey):
    operation = monkey.operation

    if operation.action == Action.ADD:
        if operation.action_on == ActionOn.SELF:
            return item + item
        else:
            return item + monkey.operation.amount
    elif operation.action == Action.MULTIPLY:
        if operation.action_on == ActionOn.SELF:
            return item * item
        else:
            return item * monkey.operation.amount

    return item


def execute_divisible(item: int, monkey: Monkey):
    is_divisible = (item % monkey.test.divisible_by) == 0
    return (is_divisible, monkey.test.divisible_by)


def get_throw_to(is_divisible: bool, monkey: Monkey):
    return monkey.test.throw_to_true if is_divisible else monkey.test.throw_to_false


def throw_to(id: int, item: int, monkeys: list[Monkey]):
    for monkey in monkeys:
        if monkey.id == id:
            monkey.items.append(item)


def print_monkey_items(data):
    for monkey in data:
        monkey.print_items()
        print()


def print_monkey_inspections(data):
    output = []
    for monkey in data:
        output.append(monkey.inspected)
        print(f'Monkey {monkey.id} inspected items {monkey.inspected} times')

    output.sort()
    return output[-1] * output[-2]


data = load_data()
# [print(line) for line in data]

print()
rounds = 20
run(data, rounds, False)

print(f'After {rounds} rounds')
print_monkey_items(data)
print(print_monkey_inspections(data))
