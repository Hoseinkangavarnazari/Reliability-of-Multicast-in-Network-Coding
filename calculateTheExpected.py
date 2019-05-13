# Read from file
f = open('Receivers2errorRate0.1.txt', 'r')
lines = f.readlines()
f.close()

statistics = [[0 for j in range(2)] for y in range(len(lines))]

# Read from file into the array
for i in range(0, len(lines)):
    lines[i] = lines[i].replace('[', '')
    lines[i] = lines[i].replace(']', '')
    lines[i] = lines[i].replace('\n', '')
    tempTotalTransmission, tempFullyDecodingProbability = lines[i].split(',')
    statistics[i][0], statistics[i][1] = float(
        tempTotalTransmission), float(tempFullyDecodingProbability)
    print(lines[i])


# Calculate the expected
expectedTransmission = statistics[0][0]*statistics[0][1]

for i in range(2, len(statistics)):
    expectedTransmission += statistics[i][0] * \
        (statistics[i][1]-statistics[i-1][1])
# x p(x) / x (p(x) - p(x-1)
print("Expected Number of total transmission:", expectedTransmission)
