filePath = '/Users/fruzki/Documents/stuff/AOC/2022/01/input.txt'
data = open(filePath, 'r')

maxSum = 0
maxSumLst = []
sum = 0
for line in data.readlines():
    if line != '\n':
        sum += int(line)
    else:
        maxSumLst.append(max(sum, maxSum))
        sum = 0

maxSumLst = [*set(maxSumLst)]
maxSumLst.sort()
lastThreeSum = sum([maxSumLst[i] for i in range(-3, -1, -1)])
# lastThreeSum = maxSumLst[-1] + maxSumLst[-2] + maxSumLst[-3]
# print(sum(maxSumLst[-3:])
print(lastThreeSum)
# print(maxSumLst[-3:])
# sum(maxSumLst[1:3])