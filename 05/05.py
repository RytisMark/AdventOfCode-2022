import re

filePath = '/Users/fruzki/Documents/stuff/AOC/2022/05/input.txt'
with open(filePath, 'r') as data:
    # lines = [line.replace("[", "").replace("]", "").replace("\n", "") for line in data]
    lines = [line.replace("\n", "") for line in data]

crateLst = []
for i in range(0, 8):
    crateLst.insert(i, lines[i])

# crateLst[0] = crateLst[0][:5] + "A" + "[ ] [ ] [ ] [ ] [ ]" + crateLst[0][31:]
crateLst[0] = "[Q] [A] [ ] [ ] [ ] [ ] [ ] [ ] [H]"
crateLst[1] = "[G] [S] [Q] [ ] [Z] [ ] [ ] [ ] [P]"
crateLst[2] = "[P] [F] [M] [ ] [F] [ ] [F] [ ] [S]"
crateLst[3] = "[R] [R] [P] [F] [V] [ ] [D] [ ] [L]"
crateLst[4] = "[L] [W] [W] [D] [W] [S] [V] [ ] [G]"
# crateLst.insert(0, "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]")
# crateLst[0] = crateLst[0][:5] + "A" + crateLst[0][6:]
# crateLst[0] = crateLst[0][:5] + " " + crateLst[0][6:]
# print(crateLst[-1][5:])


'''
[Q] [J]                         [H]
[G] [S] [Q]     [Z]             [P]
[P] [F] [M]     [F]     [F]     [S]
[R] [R] [P] [F] [V]     [D]     [L]
[L] [W] [W] [D] [W] [S] [V]     [G]
[C] [H] [H] [T] [D] [L] [M] [B] [B]
[T] [Q] [B] [S] [L] [C] [B] [J] [N]
[F] [N] [F] [V] [Q] [Z] [Z] [T] [Q]
'''

print("Pradines dezes:")
for i in range(len(crateLst)):
    print(crateLst[i])

for i in range(10, len(lines)):
    nums = re.findall(r'\d+', lines[i])
    nums = [int(x) for x in nums]
    posTake  = nums[1]*4 - 3 # position of the letter to be taken
    posPlace = nums[2]*4 - 3 # position of the letter to be placed
    while nums[0] != 0:
        rows = len(crateLst)
        for row in range(0, rows):
            if crateLst[row][posTake].isalpha():
                letter = crateLst[row][posTake]
                for k in range(-1, -rows, -1):
                    if (crateLst[k][posPlace].isalpha()) and (k == -rows):
                        crateLst.insert(0, "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]")
                        crateLst[0] = crateLst[0][:posPlace] + letter + crateLst[0][posPlace:]
                        break
                    elif (not crateLst[k][posPlace].isalpha()) and (k >= -rows):
                        crateLst[k] = crateLst[k][:posPlace] + letter + crateLst[k][posPlace:]
                        print("a")
                        break
                crateLst[row] = crateLst[row][:posTake] + " " +  crateLst[row][posTake+1:]
                break
        nums[0] -= 1

print("\nGalutines dezes:")
for i in range(len(crateLst)):
    print(crateLst[i])
    pass
