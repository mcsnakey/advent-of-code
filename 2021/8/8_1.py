FILE = "instr.txt"

count = 0

with open(FILE, 'r') as infile:
    for line in infile:
        line = line.split('|')
        num_blocks = line[1].split()
        for block in num_blocks:
            if len(block) == 2 or len(block) == 3 or len(block) == 4 or len(block) == 7:
                count += 1

print(count)
