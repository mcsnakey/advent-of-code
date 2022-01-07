from dataclasses import dataclass

FILE = "instr.txt"

@dataclass
class Board():
    board: list

    def isLowPoint(self, row, col):
        comps = []
        if row > 0:
            # check row above
            comps.append(self.board[row - 1][col])
        if row < len(self.board) - 1:
            comps.append(self.board[row + 1][col])
        if col > 0:
            comps.append(self.board[row][col - 1])
        if col < len(self.board[0]) - 1:
            comps.append(self.board[row][col + 1])
        if self.board[row][col] < min(comps):
            return True
        else:
            return False

    def calculateRisk(self):
        riskScore = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.isLowPoint(r, c):
                    riskScore += (1 + self.board[r][c])
        return riskScore

rows = []
with open (FILE, 'r') as infile:
    for line in infile:
        rows.append(list(map(int, list(line.strip()))))

b = Board(rows)
print(b.calculateRisk())
