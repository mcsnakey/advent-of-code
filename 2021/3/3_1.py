FILE = "input.txt"

flen = 0
ones_inverted = [0] * 12

with open(FILE, 'r') as infile:
    for line in infile:
        flen += 1
        line = line.strip()
        for pos in range(0, len(line)):
            if line[pos] == '1':
                ones_inverted[len(line) - pos - 1] += 1

threshold = flen // 2

gamma = 0
epsilon = 0

for idx in range(0, len(ones_inverted)):
    if ones_inverted[idx] > threshold:
        gamma += 2 ** idx
    else:
        epsilon += 2 ** idx

print(gamma * epsilon)
