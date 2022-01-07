from dataclasses import dataclass

FILE = "problem.txt"

@dataclass
class BingoBoard():
    nums: list
    marks: list

    def add_num(self, num):
        for i in range(len(self.nums)):
            if num == self.nums[i]:
                self.marks[i] = 1

    def check_win(self):
        # check horizontals
        for start in range(0, 25, 5):
            i = 0
            while i < 5 and self.marks[start + i] == 1:
                i += 1
            if i == 5:
                return True
        # check verticals
        for start in range(0, 5):
            i = 0
            while i < 5 and self.marks[start + i] == 1:
                i += 5
            if i > 24:
                return True
        return False

    def score_win(self):
        score = 0
        for i in range(len(self.nums)):
            if self.marks[i] == 0:
                score += self.nums[i]
        return score


def load_board(fd):
    line = fd.readline().strip()
    board_list = []
    while line != "":
        board_list.extend(map(int, line.split()))
        line = fd.readline().strip()
    if len(board_list) == 25:
        return BingoBoard(board_list, [0] * 25)
    else:
        return None


boards = []
call_order = None
with open(FILE, 'r') as infile:
    call_order = infile.readline().strip().split(",")
    call_order = map(int, call_order)
    infile.readline()
    board = load_board(infile)
    while board is not None:
        boards.append(board)
        board = load_board(infile)

for call in call_order:
    for board in boards:
        board.add_num(call)
        if board.check_win():
            print(board.score_win() * call)
            exit(0)