from dataclasses import dataclass, field

FILE = "instr.txt"

@dataclass
class Board():
    board: list
    allBasins: set = field(default_factory=set)

    def getNeighbors(self, row, col):
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row < len(self.board) - 1:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < len(self.board[0]) - 1:
            neighbors.append((row, col + 1))
        return neighbors

    def isLowPoint(self, row, col):
        neighbors = self.getNeighbors(row, col)
        comps = []
        for n in neighbors:
            comps.append(self.board[n[0]][n[1]])
        if self.board[row][col] < min(comps):
            return True
        else:
            return False

    def getLowPoints(self):
        lowPoints = []
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.isLowPoint(r, c):
                    lowPoints.append((r,c))
        return lowPoints

    def crawlBasin(self, thisBasin, row, col):
        thisBasin.add((row, col))
        self.allBasins.add((row, col))
        current = self.board[row][col]
        neighbors = self.getNeighbors(row, col)
        for n in neighbors:
            if n not in self.allBasins and n not in thisBasin and current < self.board[n[0]][n[1]] < 9:
                self.crawlBasin(thisBasin, n[0], n[1])

    def find_cover(self):
        lowPoints = self.getLowPoints()
        basinSizes = []
        for lp in lowPoints:
            thisBasin = set()
            self.crawlBasin(thisBasin, lp[0], lp[1])
            basinSizes.append(len(thisBasin))
        basinSizes.sort(reverse=True)
        return basinSizes[0] * basinSizes[1] * basinSizes[2]

rows = []
with open (FILE, 'r') as infile:
    for line in infile:
        rows.append(list(map(int, list(line.strip()))))

b = Board(rows)
print(b.find_cover())
