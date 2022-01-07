from dataclasses import dataclass,field
from typing import Union

hexmap = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}


@dataclass
class Packet:
    version: int
    type: int
    value: int = None


@dataclass
class Node():
    packet: Union[Packet, None]
    parent: Union["Node", None]
    children: list = field(default_factory=list)


def buildTree(bits, parent, lenCheck=False):
    version = int(bits[0:3], 2)
    type = int(bits[3:6], 2)
    if type == 4:
        intSlice = ""
        idx = 6
        while True:
            tmpSlice = bits[idx:idx + 5]
            intSlice += tmpSlice[1:]
            idx += 5
            if tmpSlice[0] == "0":
                break
        value = int(intSlice, 2)
        bits = bits[6 + len(intSlice) * 5 // 4:]
        pkt = Packet(version, type, value)
        current = Node(pkt, parent)
        parent.children.append(current)
    else:
        lenType = int(bits[6], 2)
        pkt = Packet(version, type)
        current = Node(pkt, parent)
        parent.children.append(current)
        if lenType == 0: # remaining length is lenVal
            lenVal = int(bits[7:22], 2)
            tmpBits = bits[22:22+lenVal]
            bits = bits[22+lenVal:]
            while len(tmpBits) > 0:
                tmpBits = buildTree(tmpBits, current)
        else: # packet count is lenVal
            lenVal = int(bits[7:18], 2)
            bits = bits[18:]
            for i in range(lenVal):
                bits = buildTree(bits, current)
    return bits


def evaluator(node):
    if node.packet.type == 0:
        sum = 0
        for child in node.children:
            sum += evaluator(child)
        return sum
    elif node.packet.type == 1:
        prod = 1
        for child in node.children:
            prod *= evaluator(child)
        return prod
    elif node.packet.type == 2:
        values = []
        for child in node.children:
            values.append(evaluator(child))
        return min(values)
    elif node.packet.type == 3:
        values = []
        for child in node.children:
            values.append(evaluator(child))
        return max(values)
    elif node.packet.type == 4:
        return node.packet.value
    elif node.packet.type == 5:
        diff = evaluator(node.children[0]) - evaluator(node.children[1])
        if diff > 0:
            return 1
        else:
            return 0
    elif node.packet.type == 6:
        diff = evaluator(node.children[0]) - evaluator(node.children[1])
        if diff < 0:
            return 1
        else:
            return 0
    elif node.packet.type == 7:
        diff = evaluator(node.children[0]) - evaluator(node.children[1])
        if diff == 0:
            return 1
        else:
            return 0


FILE = "input.txt"

with open(FILE, 'r') as infile:
    bitStr = ""
    hexStr = infile.readline().strip()
    for ch in hexStr:
        bitStr += hexmap[ch]

root = Node(None, None)
buildTree(bitStr, root)
print(evaluator(root.children[0]))
