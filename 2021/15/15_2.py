from dataclasses import dataclass,field
from math import inf
from heapq import *
import itertools


@dataclass
class Point():
    x: int
    y: int

    def __hash__(self):
        return (self.x, self.y).__hash__()

@dataclass
class Path():
    path: list = field(default_factory=list)
    cost: int = 0

# The following code was taken from python documentation for implementation of a priority queue.
# https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
########### BEGIN PYDOC CODE

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = None                  # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

###### END PYDOC CODE


@dataclass
class Board():
    board: dict = field(default_factory=dict)

    def neighbors(self, node):
        potential = ((-1, 0), (0, -1), (1, 0), (0, 1))
        found = set()
        for n in potential:
            if Point(node.x + n[0], node.y + n[1]) in self.board:
                found.add(Point(node.x + n[0], node.y + n[1]))
        return found

    def dijkstra(self, start):
        distance = dict()
        previous = dict()
        for point in self.board:
            add_task(point, inf)
            distance[point] = inf
            previous[point] = None
        remove_task(start)
        add_task(start, 0)
        distance[start] = 0
        while True:
            try:
                cmin = pop_task()
            except:
                break
            for n in self.neighbors(cmin):
                newdist = self.board[n] + distance[cmin]
                if newdist < distance[n]:
                    distance[n] = newdist
                    previous[n] = cmin
                    remove_task(n)
                    add_task(n, newdist)
        return distance

FILE = "input.txt"

gmap = Board()

with open(FILE, 'r') as infile:
    r = 0
    for line in infile:
        line = line.strip()
        line = list(map(int, list(line)))
        c = 0
        for val in line:
            for rowexp in range(5):
                for colexp in range(5):
                    gmap.board[Point(len(line) * colexp + c, len(line) * rowexp + r)] = (val + rowexp + colexp - 1) % 9 + 1
            c += 1
        r += 1

d=gmap.dijkstra(Point(0,0))
print(d[Point(499,499)])