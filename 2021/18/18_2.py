from dataclasses import dataclass,field
from typing import Union
from math import floor, ceil


@dataclass
class ReNode:
    parent: Union['ReNode', None]
    left: Union['ReNode', int, None]
    right: Union['ReNode', int, None]
    depth: int = 0
    onParentsLeft: bool = False
    onParentsRight: bool = False

    def __str__(self):
        return "[" + self.left.__str__() + "," + self.right.__str__() + "]"

    def __repr__(self):
        return "[" + self.left.__str__() + "," + self.right.__str__() + "]"


@dataclass
class INode:
    parent: Union[ReNode, None]
    value: int = 0
    depth: int = 0
    onParentsLeft: bool = False
    onParentsRight: bool = False

    def __str__(self):
        return self.value.__str__()

    def __repr__(self):
        return self.value.__str__()


def makeTree(inString, parent=None, depth=-1, onPLeft=False, onPRight=False):
    if inString[0] == '[' or inString[-1] == ']':
        if inString[0] == '[' and inString[-1] == ']':
            inString = inString[1:-1]
        brackCount = 0
        splitIndex = 0
        while splitIndex < len(inString) and not (inString[splitIndex] == ',' and brackCount == 0):
            if inString[splitIndex] == '[':
                brackCount += 1
            elif inString[splitIndex] == ']':
                brackCount -= 1
            splitIndex += 1
        if splitIndex == len(inString):
            raise "Parsing error - no split found in provided tuple"
        current = ReNode(parent, None, None, depth=depth+1, onParentsLeft=onPLeft, onParentsRight=onPRight)
        current.left = makeTree(inString[0:splitIndex], parent=current, depth=depth + 1, onPLeft=True)
        current.right = makeTree(inString[splitIndex+1:], parent=current, depth=depth + 1, onPRight=True)
        return current
    elif inString.isdigit():
        return INode(parent, int(inString), depth + 1, onPLeft, onPRight)
    else:
        raise "Unhandled exception in parsing"


def getLeftNode(node):
    while node.onParentsLeft:
        node = node.parent
    if node.depth == 0:
        return None
    node = node.parent.left
    while not isinstance(node, INode):
        node = node.right
    return node


def getRightNode(node):
    while node.onParentsRight:
        node = node.parent
    if node.depth == 0:
        return None
    node = node.parent.right
    while not isinstance(node, INode):
        node = node.left
    return node


def explode(node):
    leftNode = getLeftNode(node)
    rightNode = getRightNode(node)
    if leftNode is not None:
        leftNode.value += node.left.value
    if rightNode is not None:
        rightNode.value += node.right.value
    if node.onParentsLeft:
        newNode = INode(node.parent, 0, node.depth, onParentsLeft=True)
        node.parent.left = newNode
    elif node.onParentsRight:
        newNode = INode(node.parent, 0, node.depth, onParentsRight=True)
        node.parent.right = newNode
    else:
        raise "Error when exploding"
    return newNode


def split(node):
    leftVal = floor(node.value/2)
    rightVal = ceil(node.value/2)
    newNode = ReNode(node.parent, None, None, node.depth)
    newNode.left = INode(newNode, value=leftVal, depth=newNode.depth + 1, onParentsLeft=True)
    newNode.right = INode(newNode, value=rightVal, depth=newNode.depth + 1, onParentsRight=True)
    if node.onParentsLeft:
        newNode.onParentsLeft = True
        newNode.parent.left = newNode
    elif node.onParentsRight:
        newNode.onParentsRight = True
        newNode.parent.right = newNode
    else:
        raise "Error when splitting"
    return newNode

def getExplodeNode(node):
    if isinstance(node.left, INode) and isinstance(node.right, INode):
        if node.depth > 3:
            return node
        else:
            return None
    if isinstance(node.left, ReNode):
        leftCall = getExplodeNode(node.left)
        if leftCall is not None:
            return leftCall
    if isinstance(node.right, ReNode):
        rightCall = getExplodeNode(node.right)
        if rightCall is not None:
            return rightCall
    return None

def getSplitNode(node):
    if isinstance(node, INode):
        if node.value > 9:
            return node
        else:
            return None
    leftCall = getSplitNode(node.left)
    if leftCall is not None:
        return leftCall
    rightCall = getSplitNode(node.right)
    if rightCall is not None:
        return rightCall
    return None


def recIncDepth(node):
    node.depth += 1
    if isinstance(node, ReNode):
        recIncDepth(node.left)
        recIncDepth(node.right)


def simplify(tree):
    while True:
        expNode = getExplodeNode(tree)
        if expNode is not None:
            explode(expNode)
            continue
        splitNode = getSplitNode(tree)
        if splitNode is not None:
            split(splitNode)
            continue
        break


def magnitude(node):
    if isinstance(node, INode):
        return node.value
    else:
        return 3 * magnitude(node.left) + 2 * magnitude(node.right)


with open ('example.txt', 'r') as infile:
    treeStrings = []
    for line in infile:
        treeStrings.append(line.strip())

mags = []
for idx_1 in range(len(treeStrings)):
    for idx_2 in range(len(treeStrings)):
        if idx_1 == idx_2:
            continue
        tree1 = makeTree(treeStrings[idx_1])
        tree2 = makeTree(treeStrings[idx_2])
        recIncDepth(tree1)
        recIncDepth(tree2)
        combine = ReNode(None, tree1, tree2)
        combine.left.onParentsLeft = True
        combine.left.parent = combine
        combine.right.onParentsRight = True
        combine.right.parent = combine
        simplify(combine)
        mags.append(magnitude(combine))

print(max(mags))
