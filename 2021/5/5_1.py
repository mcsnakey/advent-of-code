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
    if line.start.x == line.end.x:
        # y changes
        if line.start.y < line.end.y:
            for ycord in range(line.start.y, line.end.y +1):
                plist.append(Point(line.start.x, ycord))
        elif line.start.y > line.end.y:
            for ycord in range(line.end.y, line.start.y +1):
                plist.append(Point(line.start.x, ycord))
        else:
            plist.append(line.start)
    elif line.start.y == line.end.y:
        if line.start.x < line.end.x:
            for xcord in range(line.start.x, line.end.x + 1):
                plist.append(Point(xcord, line.start.y))
        elif line.start.x > line.end.x:
            for xcord in range(line.end.x, line.start.x + 1):
                plist.append(Point(xcord, line.start.y))
        else:
            plist.append(line.start)
    else:
        return []
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