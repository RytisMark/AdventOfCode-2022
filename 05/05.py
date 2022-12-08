import re

filePath = '/Users/fruzki/Documents/stuff/AOC/2022/05/input.txt'

with open(filePath, 'r') as data:
    lines = [line.replace("\n", "") for line in data]

crateLst = []
for i in range(0, 8):
    crateLst.insert(i, lines[i])

print("Initial crates:")
for i in range(len(crateLst)):
    print(crateLst[i])
print("\n###################################")

# Part 2: change "row" to "row+nums[0]-1" (on lines 28 and 29)
for i in range(10, len(lines)):
    nums = re.findall(r'\d+', lines[i])
    nums = [int(x) for x in nums]
    posTake  = nums[1]*4 - 3
    posPlace = nums[2]*4 - 3
    while nums[0] != 0:
        rows = len(crateLst)
        rowLength = len(crateLst[0])
        for row in range(0, rows):
            if crateLst[row][posTake].isalpha():
                letter = "[" + crateLst[row][posTake] + "]" # Part 2: change row to row+nums[0]-1
                crateLst[row] = crateLst[row][:posTake-1] + "   " + crateLst[row][posTake+2:] # Part 2: change row to row+nums[0]-1
                for otherRow in range(0, rows-1):
                    if crateLst[otherRow][posPlace].isalpha():
                        crateLst.insert(0, " " * rowLength)
                        crateLst[otherRow] = crateLst[otherRow][:posPlace-1] + letter + crateLst[otherRow][posPlace:]
                        crateLst[otherRow] = crateLst[otherRow][:rowLength] + crateLst[otherRow][rowLength+2:]
                        break                     
                    elif (not crateLst[otherRow][posPlace].isalpha() and crateLst[otherRow+1][posPlace].isalpha()):
                        crateLst[otherRow] = crateLst[otherRow][:posPlace-1] + letter + crateLst[otherRow][posPlace+2:]
                        crateLst[otherRow] = crateLst[otherRow][:rowLength] + crateLst[otherRow][rowLength+2:]
                        break
                    elif (otherRow+1 == rows-1):
                        crateLst[otherRow+1] = crateLst[otherRow+1][:posPlace-1] + letter + crateLst[otherRow+1][posPlace+2:]
                        crateLst[otherRow+1] = crateLst[otherRow+1][:rowLength] + crateLst[otherRow+1][rowLength+2:]
                        break
                break
        nums[0] -= 1

for i in range(len(crateLst)):
    crateLst[i] = crateLst[i].replace(" " * 35, "")
crateLst = list(filter(None, crateLst))

print("\nEnd crates:")
for i in range(len(crateLst)):
    print(crateLst[i])
