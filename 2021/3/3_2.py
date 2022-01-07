from dataclasses import dataclass
from typing import Union

FILE = "input.txt"


@dataclass()
class BitTree:
    exp: Union[int, None] = None
    zero_ct: int = 0
    one_ct: int = 0
    zero_pt: Union['BitTree', None] = None
    one_pt: Union['BitTree', None] = None

    def __str__(self):
        return str((self.exp, self.zero_ct, self.one_ct))

    def _add_string(self, string):
        if self.exp == -1:
            return True
        ch = string[0]
        if ch == "0":
            self.zero_ct += 1
            if self.zero_pt is None:
                self.zero_pt = BitTree(self.exp - 1)
            return self.zero_pt.add_string(string[1:])
        elif ch == "1":
            self.one_ct += 1
            if self.one_pt is None:
                self.one_pt = BitTree(self.exp - 1)
            return self.one_pt.add_string(string[1:])
        else:
            return False

    def add_string(self, string):
        if self.exp is None:
            self.exp = len(string) - 1
        if self.exp == len(string) - 1:
            return self._add_string(string)
        else:
            return False

    def parse_max(self):
        if self.exp == -1:
            return 0
        elif self.zero_ct <= self.one_ct:
            return 2 ** self.exp + self.one_pt.parse_max()
        else:
            return self.zero_pt.parse_max()

    def parse_min(self):
        if self.exp == -1:
            return 0
        elif self.zero_pt is None:
            return 2 ** self.exp + self.one_pt.parse_min()
        elif self.one_pt is None:
            return self.zero_pt.parse_min()
        elif self.zero_ct <= self.one_ct:
            return self.zero_pt.parse_min()
        else:
            return 2 ** self.exp + self.one_pt.parse_min()


root = BitTree()


with open(FILE, 'r') as infile:
    for line in infile:
        root.add_string(line.strip())

print(root.parse_min() * root.parse_max())
