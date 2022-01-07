from dataclasses import dataclass
import time

@dataclass
class Point:
    a: int
    b: int
    c: int

    def orbit(self):
        pts = {}
        perms = {0: (self.a, self.b, self.c), 8: (self.c, self.a, self.b), 16: (self.b, self.c, self.a)}
        for perm in perms:
            tup = perms[perm]
            pts[perm + 0] = Point(tup[0], tup[1], tup[2])
            pts[perm + 1] = Point(tup[0], tup[2], -tup[1])
            pts[perm + 2] = Point(tup[0], -tup[1], -tup[2])
            pts[perm + 3] = Point(tup[0], -tup[2], tup[1])
            pts[perm + 4] = Point(-tup[0], tup[2], tup[1])
            pts[perm + 5] = Point(-tup[0], tup[1], -tup[2])
            pts[perm + 6] = Point(-tup[0], -tup[2], -tup[1])
            pts[perm + 7] = Point(-tup[0], -tup[1], tup[2])
        return pts

    def vector(self, final):
        return Point(final.a - self.a, final.b - self.b, final.c - self.c)

    def __hash__(self):
        return (self.a, self.b, self.c).__hash__()

    def __str__(self):
        return (self.a, self.b, self.c).__str__()

    def __repr__(self):
        return (self.a, self.b, self.c).__repr__()

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.a == other.a and self.b == other.b and self.c == other.c
        else:
            return False

ts = time.time()

scanners = dict()
board = set()

with open("input.txt", 'r') as infile:
    line = infile.readline()
    while line != "":
        line = line.strip()
        if line.strip() != "":
            if "scanner" in line:
                scanNo = int(line.strip("---").strip().split()[1])
                scanners[scanNo] = dict()
                idx = 0
            else:
                nums = tuple(map(int, line.split(',')))
                scanners[scanNo][idx] = (Point(nums[0], nums[1], nums[2]))
                idx += 1
        line = infile.readline()

for pt in scanners[0]:
    board.add(scanners[0][pt])

scan_q = []
for i in range(1, len(scanners)):
    scan_q.append(i)

while len(scan_q) > 0:
    scanidx = scan_q.pop(0)
    found = False
    print("search", scanidx)
    for fixedPoint in board:
        boardVectors = set()
        for vecPoint in board:
            if fixedPoint != vecPoint:
                boardVectors.add(fixedPoint.vector(vecPoint))
        for tmpFixedPoint in scanners[scanidx]:
            tmpVectors = dict()
            for tmpVecPoint in scanners[scanidx]:
                if tmpVecPoint != tmpFixedPoint:
                    orbits = scanners[scanidx][tmpFixedPoint].vector(scanners[scanidx][tmpVecPoint]).orbit()
                    for pt in orbits:
                        if pt not in tmpVectors:
                            tmpVectors[pt] = {orbits[pt]}
                        else:
                            tmpVectors[pt].add(orbits[pt])
            for transform in tmpVectors:
                if len(boardVectors & tmpVectors[transform]) > 10:
                    found = True
                    for vector in tmpVectors[transform]:
                        board.add(Point(fixedPoint.a + vector.a, fixedPoint.b + vector.b, fixedPoint.c + vector.c))
                    board.add(fixedPoint)
                    break
            if found:
                break
        if found:
            print("found", scanidx)
            break
    if not found:
        scan_q.append(scanidx)

print(len(board))

te = time.time()
print(te - ts)
