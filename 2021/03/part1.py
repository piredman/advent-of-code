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

def transform(input):
    output = []
    for bitIndex in range(len(input[0])):
        bits = []
        for line in input:
            bit = line[bitIndex]
            bits.append(bit)
        output.append(bits)

    return output

def getPowerConsumption(input):
    gammaRate = ''
    epsilonRate = ''
    for rate in input:
        ones = 0
        zeros = 0
        for bit in rate:
            if bit == 1:
                ones += 1
            else:
                zeros += 1
        gammaRate = gammaRate + ('1' if ones > zeros else '0')
        epsilonRate = epsilonRate + ('1' if ones < zeros else '0')

    return int(gammaRate, 2) * int(epsilonRate, 2)

diagnosticReport = loadData()
transformedReport = transform(diagnosticReport)
powerConsumption = getPowerConsumption(transformedReport)
print(powerConsumption)