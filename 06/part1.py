import csv
fileName = '06/input.txt'
days = 80
school = []


def loadData():
    output = []
    with open(fileName, 'r', newline='') as fileData:
        reader = csv.reader(fileData, delimiter=',')
        row = next(reader)
        output = [int(x) for x in row]

    return output


def progressDay():
    newFish = 0
    for index, fish in enumerate(school):
        if fish == 0:
            newFish += 1
            school[index] = 6
            continue

        school[index] -= 1

    for fish in list(range(newFish)):
        school.append(8)


school = loadData()
for day in list(range(days)):
    progressDay()

print()
print(f"There are {len(school)} fish in the school after {days} days")
