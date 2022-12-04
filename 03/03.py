# Day 3
filePath = '/Users/fruzki/Documents/stuff/AOC/2022/03/input.txt'

abc = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 2
with open(filePath, 'r') as data:
    lines = [line.rstrip() for line in data]

prioritiesSum = 0
for i in range(0, len(lines), 3):
    for j in range(len(lines[i])):
        if (lines[i][j] in lines[i+1]) and (lines[i][j] in lines[i+2]):
            prioritiesSum += abc.index(lines[i][j])
            break
print(prioritiesSum)

'''
# Part 1
data = open(filePath, 'r')

prioritiesSum = 0
for line in data.readlines():
    halfLength = int(len(line)/2)
    compartmentOne = line[0:halfLength]
    compartmentTwo = line[halfLength:halfLength*2]

    for i in range(len(compartmentOne)):
        if (compartmentOne[i] in compartmentTwo):
            prioritiesSum += abc.index(compartmentOne[i])
            break

print(prioritiesSum)
'''