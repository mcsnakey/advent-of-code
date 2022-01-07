FILE = "nums.txt"

greaterThans = 0

with open(FILE, 'r') as infile:
    slot_L = int(infile.readline().strip())
    slot_C = int(infile.readline().strip())
    slot_R = int(infile.readline().strip())
    thisSum = slot_L + slot_C + slot_R
    num = infile.readline().strip()
    while num != "":
        lastSum = thisSum
        slot_L = slot_C
        slot_C = slot_R
        slot_R = int(num)
        thisSum = slot_L + slot_C + slot_R
        if thisSum > lastSum:
            greaterThans += 1
        num = infile.readline().strip()

print(greaterThans)
