# Day 2

# Both parts
# 0 lost
# 3 draw
# 6 win

# Part 1
# 1 for rock A X
# 2 for paper B Y
# 3 for scissors C Z
# ABC - foe. XYZ - you

# Part 2
# X - lose
# Y - draw
# Z - win

filePath = '/Users/fruzki/Documents/stuff/AOC/2022/02/input.txt'
data = open(filePath, 'r')

# Part 2
pointsTotal = 0
for line in data.readlines():
    roundData = line.rstrip()

    if roundData[2] == "X":
        pointsTotal += 0
        if roundData[0] == "A":
            pointsTotal += 3
        elif roundData[0] == "B":
            pointsTotal += 1
        elif roundData[0] == "C":
            pointsTotal += 2

    elif roundData[2] == "Y":
        pointsTotal += 3
        if roundData[0] == "A":
            pointsTotal += 1
        elif roundData[0] == "B":
            pointsTotal += 2
        elif roundData[0] == "C":
            pointsTotal += 3

    elif roundData[2] == "Z":
        pointsTotal += 6
        if roundData[0] == "A":
            pointsTotal += 2
        elif roundData[0] == "B":
            pointsTotal += 3
        elif roundData[0] == "C":
            pointsTotal += 1
print(pointsTotal)


'''
# Part 1
pointsTotal = 0
for line in data.readlines():
    roundData = line.rstrip()
    if roundData[2] == "X":
        pointsTotal += 1
        if roundData[0] == "A":
            pointsTotal += 3
        elif roundData[0] == "B":
            pointsTotal += 0
        elif roundData[0] == "C":
            pointsTotal += 6

    elif roundData[2] == "Y":
        pointsTotal += 2
        if roundData[0] == "A":
            pointsTotal += 6
        elif roundData[0] == "B":
            pointsTotal += 3
        elif roundData[0] == "C":
            pointsTotal += 0

    elif roundData[2] == "Z":
        pointsTotal += 3
        if roundData[0] == "A":
            pointsTotal += 0
        elif roundData[0] == "B":
            pointsTotal += 6
        elif roundData[0] == "C":
            pointsTotal += 3
print(pointsTotal)
'''
