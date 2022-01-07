from dataclasses import dataclass
import queue
import time

FILE = "example.txt"


def advance(position, spaces):
    return (position + spaces - 1) % 10 + 1

sto = dict()

def playgame(turn, p1pos, p1pts, p2pos, p2pts, dieFreq, mems):
    if p1pts >= 21:
        return 1, 0
    if p2pts >= 21:
        return 0, 1
    onewon = 0
    twowon = 0
    if turn == 1:
        # Player 1's turn
        for roll in dieFreq:
            newPos = advance(p1pos, roll)
            newPts = p1pts + newPos
            memTup = (2, newPos, newPts, p2pos, p2pts)
            if memTup not in mems:
                mems[memTup] = playgame(2, newPos, newPts, p2pos, p2pts, dieFreq, mems)
            onewon += mems[memTup][0] * dieFreq[roll]
            twowon += mems[memTup][1] * dieFreq[roll]
    elif turn == 2:
        # Player 2's turn
        for roll in dieFreq:
            newPos = advance(p2pos, roll)
            newPts = p2pts + newPos
            memTup = (1, p1pos, p1pts, newPos, newPts)
            if memTup not in mems:
                mems[memTup] = playgame(1, p1pos, p1pts, newPos, newPts, dieFreq, mems)
            onewon += mems[memTup][0] * dieFreq[roll]
            twowon += mems[memTup][1] * dieFreq[roll]
    else:
        raise Exception("A turn has begun with invalid player:" + str(turn))
    return onewon, twowon

ts = time.time()

dieFreq = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

g = playgame(1, 4, 0, 10, 0, dieFreq, sto)
print(max(g))

te = time.time()
print(te - ts)
