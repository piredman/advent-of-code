import csv
from enum import IntEnum

class Instruction(IntEnum):
    DIRECTION = 0
    AMOUNT = 1

class Position(IntEnum):
    HORIZONTAL = 0
    DEPTH = 1
    AIM = 2

# horizontal, depth, aim
position = [0, 0, 0]

def loadData():
    instructionData = []
    with open('02/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            rowData = str.split(row[0])
            instruction = [rowData[0], int(rowData[1])]
            instructionData.append(instruction)

    return instructionData

def execute(instructions):
    for instruction in instructions:
        move(instruction)

def move(instruction):
    print(instruction)
    direction = instruction[int(Instruction.DIRECTION)] 
    amount = instruction[int(Instruction.AMOUNT)]

    if (direction == 'forward'):
        forward(amount)
        return

    if (direction == 'down'):
        down(amount)
        return

    if (direction == 'up'):
        up(amount)
        return
    
def forward(value):
    depthValue = position[int(Position.AIM)] * value
    position[int(Position.DEPTH)] = position[int(Position.DEPTH)] + depthValue
    position[int(Position.HORIZONTAL)] = position[int(Position.HORIZONTAL)] + value

def down(value):
    position[int(Position.AIM)] = position[int(Position.AIM)] + value

def up(value):
    position[int(Position.AIM)] = position[int(Position.AIM)] - value

def sumPosition():
    return position[int(Position.HORIZONTAL)] * position[int(Position.DEPTH)]

data = loadData()
execute(data)
print(position)
print(sumPosition())