import csv
import array

hands = {
    'ROCK': {
        'match': ['A', 'X'],
        'value': 1
    },
    'PAPER': {
        'match': ['B', 'Y'],
        'value': 2
    },
    'SCISSORS': {
        'match': ['C', 'Z'],
        'value': 3
    },
}


def loadData():
    input = []
    with open('02/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            for column in row:
                them = matchHand(column[0])
                you = matchHand(column[2])
                round = {
                    'them': them,
                    'you': you
                }
                matchResult = play(round)
                input.append(round["you"][1] + matchResult)

    return input


def matchHand(input):
    result = {}

    for handName in hands:
        hand = hands[handName]
        match = hand['match']
        if any(input in x for x in match):
            result = [handName, hand['value']]
            break

    return result


def play(input):
    them = input['them'][0]
    you = input['you'][0]

    if them == you:
        return 3

    if (you == 'ROCK' and them == 'SCISSORS') or \
        (you == 'SCISSORS' and them == 'PAPER') or \
            (you == 'PAPER' and them == 'ROCK'):
        return 6

    return 0


data = loadData()
print(data)
print(sum(data))
