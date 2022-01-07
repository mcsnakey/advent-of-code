from dataclasses import dataclass

FILE = "instr.txt"


@dataclass
class Point():
    x: int
    y: int

    def __hash__(self):
        return (self.x, self.y).__hash__()

@dataclass
class Line():
    start: Point
    end: Point


def parse_line(line):
    line_arr = line.split()
    s_arr = line_arr[0].split(',')
    e_arr = line_arr[2].split(',')
    return Line(Point(int(s_arr[0]), int(s_arr[1])), Point(int(e_arr[0]), int(e_arr[1])))

def get_points(line):
    plist = []
    xmin = min(line.start.x, line.end.x)
    ymin = min(line.start.y, line.end.y)
    xmax = max(line.start.x, line.end.x)
    ymax = max(line.start.y, line.end.y)
    if xmax - xmin == 0 or ymax - ymin == 0:
        for xcord in range(xmin, xmax + 1):
            for ycord in range(ymin, ymax + 1):
                plist.append(Point(xcord, ycord))
    elif ymax - ymin == xmax - xmin:
        delta = xmax - xmin
        ydelt = line.end.y - line.start.y
        xdelt = line.end.x - line.start.x
        if (ydelt // xdelt>0):
            # positive
            for i in range(0, delta + 1):
                plist.append(Point(xmin + i, ymin + i))
        else:
            # negative
            for i in range(0, delta + 1):
                plist.append(Point(xmin + i, ymax - i))
    else:
        raise "Issue we didn't consider..."
    return plist


line_array = []

with open(FILE, 'r') as infile:
    for line in infile:
        line = line.strip()
        line_array.append(parse_line(line))

max_num = 0
for line in line_array:
    numtmp = max(line.start.x, line.start.y, line.end.x, line.end.y)
    if numtmp > max_num:
        max_num = numtmp


d = dict()
for x in range(0, max_num + 1):
    for y in range(0, max_num + 1):
        d[Point(x,y)] = 0

for line in line_array:
    pts = get_points(line)
    for pt in pts:
        d[pt] += 1

ct = 0
for pt in d:
    if d[pt] > 1:
        ct += 1

print(ct)