from dataclasses import dataclass,field

FILE = "instr.txt"

class FishPool():
    def __init__(self, days):
        self.days = days
        self.pool = dict()
        for day in range(0, days + 1 + 8):
            self.pool[day] = 0

    def add_fish(self, days):
        self.pool[days] += 1

    def simulate_day(self, zero_day):
        newFish = self.pool[zero_day]
        self.pool[zero_day + 7] += newFish
        self.pool[zero_day + 9] += newFish

    def fish_sum(self):
        summ = 0
        for i in range(self.days, len(self.pool)):
            summ += self.pool[i]
        return summ

    def simulate(self):
        for day in range(self.days):
            self.simulate_day(day)
        return self.fish_sum()


with open(FILE, 'r') as infile:
    arr = list(map(int, infile.readline().strip().split(',')))
    fp = FishPool(256)
    for fish in arr:
        fp.add_fish(fish)
    print(fp.simulate())
