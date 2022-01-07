FILE = "instr.txt"
numsteps = 40

with open(FILE, 'r') as infile:
    polymer_s = infile.readline().strip()
    mapping = dict()
    infile.readline()
    line = infile.readline().strip()
    while line != "":
        split = line.split()
        mapping[split[0]] = split[2]
        line = infile.readline().strip()

polymer = dict()
counts = dict()

for idx in range(len(polymer_s) - 1):
    code = polymer_s[idx:idx+2]
    if code not in polymer:
        polymer[code] = 1
    else:
        polymer[code] += 1
    if polymer_s[idx] not in counts:
        counts[polymer_s[idx]] = 1
    else:
        counts[polymer_s[idx]] += 1
end = polymer_s[-1]
if end not in counts:
    counts[end] = 1
else:
    counts[end] += 1

for step in range(1, numsteps + 1):
    newPoly = dict()
    for code in polymer:
        if code in mapping:
            mapch = mapping[code]
            left = code[0] + mapch
            right = mapch + code[1]
            if left not in newPoly:
                newPoly[left] = polymer[code]
            else:
                newPoly[left] += polymer[code]
            if right not in newPoly:
                newPoly[right] = polymer[code]
            else:
                newPoly[right] += polymer[code]
            if mapch not in counts:
                counts[mapch] = polymer[code]
            else:
                counts[mapch] += polymer[code]
        else:
            if code not in newPoly:
                newPoly[code] = polymer[code]
            else:
                newPoly[code] += polymer[code]
    polymer = newPoly

count_list = []
for let in counts:
    count_list.append(counts[let])
count_list.sort()

print(count_list[-1] - count_list[0])
