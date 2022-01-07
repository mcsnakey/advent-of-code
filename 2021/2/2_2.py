FILE = "instr.txt"

x = 0
y = 0
aim = 0

with open(FILE, 'r') as infile:
    line = infile.readline().strip()
    while line != "":
        split = line.split()
        way = split[0]
        val = int(split[1])
        if way == "forward":
            x += val
            y += aim * val
        elif way == "up":
            aim -= val
        elif way == "down":
            aim += val
        line = infile.readline().strip()

print(x*y)
