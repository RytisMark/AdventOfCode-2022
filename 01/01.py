filePath = '/Users/fruzki/Documents/stuff/AOC/2022/01/input.txt'
data = open(filePath, 'r')

maxSum = 0
maxSumLst = []
totalSum = 0
for line in data.readlines():
    if line != '\n':
        totalSum += int(line)
    else:
        maxSumLst.append(max(totalSum, maxSum))
        totalSum = 0

maxSumLst = [*set(maxSumLst)]
maxSumLst.sort()
print(maxSumLst[-1])
lastThreeSum = sum(maxSumLst[-3:])
print(lastThreeSum)
