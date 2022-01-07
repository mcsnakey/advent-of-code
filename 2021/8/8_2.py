FILE = "instr.txt"

run_sum = 0

with open(FILE, 'r') as infile:
    for line in infile:
        line = line.split('|')
        chunks = list(map(set, line[0].split()))
        n = [set()] * 10
        for i in range(len(chunks)):
            if len(chunks[i]) == 2:
                n[1] = chunks[i]
                chunks[i] = set()
            elif len(chunks[i]) == 3:
                n[7] = chunks[i]
                chunks[i] = set()
            elif len(chunks[i]) == 4:
                n[4] = chunks[i]
                chunks[i] = set()
            elif len(chunks[i]) == 7:
                n[8] = chunks[i]
                chunks[i] = set()
        for i in range(len(chunks)):
            if len(chunks[i]) == 6 and len(chunks[i] - (n[7] | n[4])) == 1:
                n[9] = chunks[i]
                chunks[i] = set()
        for i in range(len(chunks)):
            if len(chunks[i]) == 6 and len(chunks[i] & n[1]) == 2:
                n[0] = chunks[i]
                chunks[i] = set()
        for i in range(len(chunks)):
            if len(chunks[i]) == 6:
                n[6] = chunks[i]
                chunks[i] = set()
        for i in range(len(chunks)):
            if len(chunks[i]) == 5 and len(chunks[i] & n[1]) == 2:
                n[3] = chunks[i]
                chunks[i] = set()
        for i in range(len(chunks)):
            if len(chunks[i]) == 5 and len(chunks[i] & (n[8] - n[9])) == 1:
                n[2] = chunks[i]
                chunks[i] = set()
        for i in range(len(chunks)):
            if len(chunks[i]) == 5:
                n[5] = chunks[i]
                chunks[i] = set()
        output = list(map(set, line[1].split()))
        power = 1
        for i in range(len(output) - 1, -1, -1):
            for j in range(len(n)):
                if len(output[i]) == len(n[j]) and len(output[i]) == len(output[i] & n[j]):
                    run_sum += j * power
                    power *= 10
                    break
print(run_sum)
