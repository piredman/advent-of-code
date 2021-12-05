import csv

def loadData():
    output = []
    with open('03/input.txt', newline='') as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            line = []
            for column in row[0]:
                line.append(int(column))
            output.append(line)

    return output

def getCounts(input, index):
    ones = 0
    zeros = 0

    for line in input:
        if line[index] == 1:
            ones += 1
        else:
            zeros += 1
    
    return [ones, zeros]

def oxygenCriteria(ones, zeros):
    return 1 if ones >= zeros else 0

def co2Criteria(ones, zeros):
    return 0 if ones >= zeros else 1

def getMatches(input, index, searchValue):
    output = []
    for line in input:
        if line[index] == searchValue:
            output.append(line)

    return output

def getRating(input, criteriaFn):
    count = len(input)
    result = input
    for bitIndex in range(count):
        counts = getCounts(result, bitIndex)
        searchText = criteriaFn(counts[0], counts[1])
        result = getMatches(result, bitIndex, searchText)
        if (len(result)) <= 1:
            break
    
    binary = "".join(str(x) for x in result[0])
    return int(binary, 2)

def getLifeSupportRating(input):
    oxygenRating = getRating(input, oxygenCriteria)
    co2Rating = getRating(input, co2Criteria)
    return oxygenRating * co2Rating

data = loadData()
result = getLifeSupportRating(data)
print(result)