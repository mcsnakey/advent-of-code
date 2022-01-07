FILE = "input.txt"

def getNeighborString(point, board, boardmin, boardmax, boundsPc):
    transforms = [(-1,-1), (0,-1), (1,-1), (-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1)]
    ptString = ""
    for trans in transforms:
        pt = (point[0] + trans[0], point[1] + trans[1])
        if pt[0] <= boardmin or pt[0] >= boardmax or pt[1] <= boardmin or pt[1] >= boardmax:
            ptString += boundsPc
        elif pt not in board:
            ptString += '.'
        else:
            ptString += "#"
    return ptString

def string2int(string):
    if len(string) == 0:
        return 0
    if string[0] == '#':
        return 2 ** (len(string) - 1) + string2int(string[1:])
    else:
        return string2int(string[1:])

image = set()

with open(FILE, 'r') as infile:
    expansion = list(infile.readline().strip())
    infile.readline()
    y = 0
    line = infile.readline().strip()
    while line != "":
        for chidx in range(len(line)):
            if line[chidx] == "#":
                image.add((chidx, y))
        line = infile.readline().strip()
        y += 1

boardMin = 0
boardMax = y - 1

def printImage(img, low, hi):
    for y in range(low, hi + 1):
        for x in range(low, hi + 1):
            if (x,y) in img:
                print('#', end="")
            else:
                print(".", end="")
        print()

#printImage(image, boardMin, boardMax)

expandRounds = 50
edgePc = '.'
for round in range(expandRounds):
    boardMin -= 1
    boardMax += 1
    newImg = set()
    for x in range(boardMin, boardMax + 1):
        for y in range(boardMin, boardMax + 1):
            s = string2int(getNeighborString((x, y), image, boardMin, boardMax, edgePc))
            if expansion[s] == "#":
                newImg.add((x, y))
    image = newImg
    edgePc = expansion[string2int(9 * edgePc)]

print(len(image))