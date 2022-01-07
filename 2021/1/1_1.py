FILE = "nums.txt"

lastNum = -1
greaterThans = -1

with open(FILE, 'r') as infile:
    for line in infile:
        num = int(line.strip())
        if num > lastNum:
            greaterThans += 1
        lastNum = num

print(greaterThans)