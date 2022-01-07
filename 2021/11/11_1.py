from dataclasses import dataclass
from math import sqrt
import queue

FILE = "instr.txt"

@dataclass
class Board:
    arr: list
    flashCount: int = 0
    turnVisited = None
    turnQueue = None

    def print(self):
        for i in range(0, 100, 10):
            for ch in self.arr[i:i+10]:
                print(ch, end="")
            print()
        print()

    def print2(self):
        for i in range(0, len(self.arr), int(sqrt(len(self.arr)))):
            for j in range(i, i+int(sqrt(len(self.arr)))):
                print(f"{self.arr[j]:3d}", end="")
            print()
        print()

    def addOnes(self):
        for i in range(len(self.arr)):
            self.arr[i] += 1

    def flash(self, idx):
        if idx in self.turnVisited:
            return
        self.turnVisited.add(idx)
        self.flashCount += 1
        sqt = int(sqrt(len(self.arr)))
        tgts = [-(sqt+1), -sqt, -(sqt-1), -1, 1, sqt-1, sqt, sqt+1]
        if idx % 10 == 0:
            # we're on the left... don't check for things to the left
            tgts.remove(-(sqt+1))
            tgts.remove(-1)
            tgts.remove(sqt-1)
        elif idx % 10 == 9:
            # we're on the right... don't check for things on the right
            tgts.remove(1)
            tgts.remove(-(sqt-1))
            tgts.remove(sqt + 1)
        for tgt in tgts:
            if 0 <= idx + tgt < len(self.arr):
                self.arr[idx + tgt] += 1
                if self.arr[idx + tgt] > 9 and (idx + tgt) not in self.turnVisited:
                    self.turnQueue.put(idx + tgt)

    def setZeros(self):
        for i in range(len(self.arr)):
            if self.arr[i] > 9:
                self.arr[i] = 0

    def run_round(self):
        self.addOnes()
        self.turnQueue = queue.Queue()
        self.turnVisited = set()
        for i in range(len(self.arr)):
            if self.arr[i] > 9:
                self.turnQueue.put(i)
        while not self.turnQueue.empty():
            xy = self.turnQueue.get()
            self.flash(xy)
        self.setZeros()


with open(FILE, 'r') as infile:
    numstr = ""
    for line in infile:
        numstr += line.strip()
    nums = list(map(int, list(numstr)))

x = Board(nums)
i = 0
while True:
    i += 1
    x.run_round()
    if sum(x.arr) == 0:
        print(i)
        break