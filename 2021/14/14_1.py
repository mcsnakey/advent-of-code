FILE = "instr.txt"
numsteps = 40

with open(FILE, 'r') as infile:
    polymer = infile.readline().strip()
    mapping = dict()
    infile.readline()
    line = infile.readline().strip()
    while line != "":
        split = line.split()
        mapping[split[0]] = split[2]
        line = infile.readline().strip()

for step in range(1, numsteps + 1):
    newPoly = ""
    for idx in range(len(polymer) - 1):
        if polymer[idx:idx+2] in mapping:
            newPoly += polymer[idx] + mapping[polymer[idx:idx+2]]
        else:
            newPoly += polymer[idx]
    newPoly += polymer[-1]
    polymer = newPoly
    print(step)

counts = dict()
for char in polymer:
    if char not in counts:
        counts[char] = 0
    counts[char] += 1

counts_list = []
for num in counts:
    counts_list.append(counts[num])
counts_list.sort()

print(counts_list[-1] - counts_list[0])