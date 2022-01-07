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

sum = 0

with open (FILE, 'r') as infile:
    for line in infile:
        line = list(line.strip())
        stack = queue.LifoQueue()
        for sym in line:
            if sym in open_syms:
                stack.put(sym)
            elif sym in close_syms:
                elem = stack.get()
                if not matches(elem, sym):
                    if sym == ')':
                        sum += 3
                    elif sym == ']':
                        sum += 57
                    elif sym == '}':
                        sum += 1197
                    elif sym == '>':
                        sum += 25137

print(sum)