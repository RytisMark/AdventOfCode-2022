filePath = '/Users/fruzki/Documents/stuff/AOC/2022/06/input.txt'

dataStream = open(filePath, 'r').readlines()[0]

# length = 4 # Part 1
length = 14 # Part 2
checkLst = [dataStream[i] for i in range(0, length)]
while len(set(checkLst)) != len(checkLst):
        checkLst.pop(0)
        checkLst.append(dataStream[length])
        length += 1
print(length)