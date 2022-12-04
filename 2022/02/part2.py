import csv
import array

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'
LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

hands = {
    ROCK: {
        'value': 1,
        'self': ROCK,
        'win': SCISSORS,
        'lose': PAPER
    },
    PAPER: {
        'value': 2,
        'self': PAPER,
        'win': ROCK,
        'lose': SCISSORS
    },
    SCISSORS: {
        'value': 3,
        'self': SCISSORS,
        'win': PAPER,
        'lose': ROCK
    },
}


def loadData():
    input = []
    with open('02/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            for column in row:
                them = matchHand(column[0])
                you = pickHand(them, column[2])
                playResult = play(them, you)
                input.append(you['value'] + playResult)

    return input


def matchHand(input):
    result = {}

    for hand in hands:
        if hand == input:
            result = hands[hand]
            break

    return result


def pickHand(them, expected):
    if expected == WIN:
        return hands[them['lose']]

    if expected == LOSE:
        return hands[them['win']]

    return them


def play(them, you):
    if you['win'] == them['self']:
        return 6

    if you['lose'] == them['self']:
        return 0

    return 3


data = loadData()
print(sum(data))
