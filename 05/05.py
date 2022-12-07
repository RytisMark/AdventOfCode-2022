import re

filePath = '/Users/fruzki/Documents/stuff/AOC/2022/05/input.txt'
with open(filePath, 'r') as data:
    lines = [line.replace("[", "").replace("]", "").replace("\n", "") for line in data]

crateLst = []
for i in range(0, 8):
    crateLst.insert(i, lines[i])

print(crateLst)
# for i in range(10, len(lines)):
#     nums = re.findall(r'\d+', lines[i])
#     while(nums[0] != 0):
#         for j in range(0, len(crateLst)):
#             if crateLst[j][int(nums[1]*2)] != " ":
#                 for k in range(-1, len(crateLst)):
                    
#                     pass
#                 break
#             else:
#                 continue
#         nums[0] -= 1
