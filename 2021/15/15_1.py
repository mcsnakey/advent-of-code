from dataclasses import dataclass,field
from math import inf
import heapq


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
        unvisited = set(self.board)
        previous = dict()
        for point in self.board:
            distance[point] = inf
            previous[point] = None
        distance[start] = 0
        while len(unvisited) > 0:
            cmin = None
            for node in unvisited:
                if cmin is None:
                    cmin = node
                elif distance[node] < distance[cmin]:
                    cmin = node
            unvisited.remove(cmin)
            for n in self.neighbors(cmin):
                newdist = self.board[n] + distance[cmin]
                if newdist < distance[n]:
                    distance[n] = newdist
                    previous[n] = cmin
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
            gmap.board[Point(c, r)] = val
            c += 1
        r += 1

d = gmap.dijkstra(Point(0,0))
print(d[Point(99,99)])
