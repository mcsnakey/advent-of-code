import queue

open_syms = {'[', '(', '{', '<'}
close_syms = {']', ')', '}', '>'}

FILE = "input.txt"

def matches(left, right):
    if left == '(':
        return right == ')'
    elif left == '[':
        return right == ']'
    elif left == '{':
        return right == '}'
    elif left == '<':
        return right == '>'

sums = []

with open (FILE, 'r') as infile:
    for line in infile:
        not_corrupted = True
        linesum = 0
        line = list(line.strip())
        stack = queue.LifoQueue()
        for sym in line:
            if sym in open_syms:
                stack.put(sym)
            elif sym in close_syms:
                elem = stack.get()
                if not matches(elem, sym):
                    not_corrupted = False

        while not_corrupted and stack.qsize() > 0:
            linesum *= 5
            left = stack.get()
            if left == '(':
                linesum += 1
            elif left == '[':
                linesum += 2
            elif left == '{':
                linesum += 3
            elif left == '<':
                linesum += 4
        if not_corrupted:
            sums.append(linesum)

sums.sort()
print(sums[len(sums)//2])
