import re
filePath = '/Users/fruzki/Documents/stuff/AOC/2022/04/input.txt'

with open(filePath, 'r') as data:
    lines = [line.replace("\n", "").replace(",", "-") for line in data]

# Part 2
rangeOverlap = 0
for line in lines:
    nums = re.findall(r'\b\d+\b', line)
    if (int(nums[0]) <= int(nums[3])) and (int(nums[1]) >= int(nums[2])):
        rangeOverlap += 1
print(rangeOverlap)

'''
# Part 1
rangedFully = 0
for line in lines:
    nums = re.findall(r'\b\d+\b', line)
    if (int(nums[0]) <= int(nums[2])) and (int(nums[1]) >= int(nums[3])):
        rangedFully += 1
    elif (int(nums[2]) <= int(nums[0])) and (int(nums[3]) >= int(nums[1])):
        rangedFully += 1
    print(nums)
print(rangedFully)
'''