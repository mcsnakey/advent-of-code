from dataclasses import dataclass
import queue

FILE = "example.txt"

@dataclass
class Player:
    position: int = 0
    score: int = 0

    def won(self):
        return self.score >= 1000

    def play(self, spaces):
        self.position = (self.position + spaces - 1) % 10 + 1
        self.score += self.position
        return self.won()

@dataclass
class DDie:
    turns = 0

    def roll(self):
        val = (self.turns * 3 + 1) * 3 + 3
        self.turns += 1
        return val


p1 = Player(position=4)
p2 = Player(position=10)

players = queue.Queue()
players.put(p1)
players.put(p2)

die = DDie()
won = False
while not won:
    turn = players.get()
    won = turn.play(die.roll())
    if not won:
        players.put(turn)

print(players.get().score * die.turns * 3)