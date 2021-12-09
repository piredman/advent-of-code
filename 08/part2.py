import csv
fileName = '08/input.txt'


def loadData():
    output = []
    with open(fileName, 'r', newline='') as fileData:
        reader = csv.reader(fileData, delimiter='|')
        for row in reader:
            line = []
            for column in row:
                line.append(list(filter(None, column.split(' '))))
            output.append(line)

    return output


def matchUniques(input):
    keys = []
    for item in input:
        length = len(item)
        if length == 2:
            keys.append([1, item])
        elif length == 3:
            keys.append([7, item])
        elif length == 4:
            keys.append([4, item])
        elif length == 7:
            keys.append([8, item])

    return keys


def getNumber(input, number):
    output = []
    for item in input:
        if item[0] == number:
            output = item
            break

    return output


def getCounts(input, characters):
    count = 0
    for character in characters:
        if character in input:
            count += 1

    return count


def matchFives(input, keys):
    for item in input:
        if len(item) == 5:
            one = getNumber(keys, 1)[1]
            count = getCounts(item, one)
            if len(one) == count:
                keys.append([3, item])
                continue

            four = getNumber(keys, 4)[1]
            count = getCounts(item, four)
            if count == 2:
                keys.append([2, item])
                continue

            keys.append([5, item])


def matchSixes(input, keys):
    for item in input:
        if len(item) == 6:
            one = getNumber(keys, 1)[1]
            count = getCounts(item, one)
            if len(one) != count:
                keys.append([6, item])
                continue

            four = getNumber(keys, 4)[1]
            count = getCounts(item, four)
            if len(four) == count:
                keys.append([9, item])
                continue

            keys.append([0, item])


data = loadData()

finalValues = []
for line in data:
    input = line[0]
    keys = matchUniques(input)
    matchFives(input, keys)
    matchSixes(input, keys)

    input = line[1]
    stringValue = ''
    for item in input:
        for key in keys:
            value = key[1]
            count = getCounts(item, value)
            if len(item) == count and len(item) == len(value):
                stringValue += str(key[0])
                break

    finalValue = int(stringValue)
    print(f"{input}: {finalValue}")
    finalValues.append(finalValue)

print(f"sum: {sum(finalValues)}")
