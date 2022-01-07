from dataclasses import dataclass,field

@dataclass
class Probe():
    x_vel: int
    y_vel: int
    x_pos: int = 0
    y_pos: int = 0

    def step(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        if self.x_vel > 0:
            self.x_vel -= 1
        elif self.x_vel < 0:
            self.x_vel += 1
        self.y_vel -= 1

@dataclass
class GameBoard():
    left: int
    right: int
    bottom: int
    top: int
    hits: dict = field(default_factory=dict)

    def fire_shot(self, x_vel, y_vel):
        p = Probe(x_vel, y_vel)
        y_max = 0
        while p.x_pos <= self.right and p.y_pos >= self.bottom:
            if p.y_pos > y_max:
                y_max = p.y_pos
            if self.left <= p.x_pos and p.y_pos <= self.top:
                self.hits[(x_vel, y_vel)] = y_max
                break
            else:
                p.step()
        return p


FILE = "input.txt"

with open(FILE, 'r') as infile:
    line = infile.readline().strip()
    line = line.split()
    xlist = list(map(int, line[2][2:-1].split("..")))
    ylist = list(map(int, line[3][2:].split("..")))
    gb = GameBoard(xlist[0], xlist[1], ylist[0], ylist[1])

for x0 in range(0, gb.right + 2):
    for y0 in range(-abs(gb.bottom), abs(gb.bottom) + 1):
        p = gb.fire_shot(x0, y0)

print(len(gb.hits))
