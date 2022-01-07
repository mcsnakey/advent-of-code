from dataclasses import dataclass,field

@dataclass
class Point():
    x: int
    y: int

    def __hash__(self):
        return (self.x, self.y).__hash__()

@dataclass
class Paper():
    points: field(default_factory=set)
    folds: field(default_factory=list)

    def fold_x(self, axis):
        newPoints = set()
        for point in self.points:
            if point.x != axis:
                newPoints.add(Point(abs(point.x - axis) - 1, point.y))
            else:
                raise "This shouldn't happen..."
        self.points = newPoints

    def fold_y(self, axis):
        newPoints = set()
        for point in self.points:
            if point.y != axis:
                newPoints.add(Point(point.x, (abs(point.y - axis) - 1)))
            else:
                raise "This shouldn't happen..."
        self.points = newPoints

    def process_folds(self):
        for fold in folds:
            if fold[0] == 'y':
                self.fold_y(fold[1])
            elif fold[0] == 'x':
                self.fold_x(fold[1])
            else:
                raise "This shouldn't happen..."

    def print(self):
        xmax = 0
        ymax = 0
        for point in self.points:
            if point.x > xmax:
                xmax = point.x
            if point.y > ymax:
                ymax = point.y
        for y_idx in range(ymax, -1, -1):
            for x_idx in range(xmax, -1, -1):
                if Point(x_idx, y_idx) in self.points:
                    print("#", end="")
                else:
                    print(".", end="")
            print()


FILE = "instr.txt"

with open(FILE, 'r') as infile:
    points = []
    folds = []
    divHit = False
    for line in infile:
        line = line.strip()
        if line == "":
            divHit = True
            continue
        if divHit:
            line = line.split()[2].split('=')
            folds.append((line[0], int(line[1])))
        else:
            line = list(map(int, line.split(',')))
            points.append(Point(line[0], line[1]))

paper = Paper(points, folds)
paper.process_folds()
paper.print()
