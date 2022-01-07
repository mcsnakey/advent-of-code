FILE = "example.txt"

graph = dict()

with open(FILE, 'r') as infile:
    for line in infile:
        line = line.strip().split('-')
        if line[0] not in graph:
            graph[line[0]] = set()
        graph[line[0]].add(line[1])
        if line[1] not in graph:
            graph[line[1]] = set()
        graph[line[1]].add(line[0])


def isLittle(node):
    if node == "start" or node == "end":
        return False
    else:
        return node.islower()


def isBig(node):
    return node.isupper()

paths = []
path = ["start"]
visited = {"start"}

print(visited)

def crawler(node, cpath, graph, visited):
    if node == "end":
        paths.append(tuple(cpath))
        return
    else:
        for n in graph[node]:
            if n not in visited:
                if isLittle(n):
                    visited.add(n)
                cpath.append(n)
                crawler(n, cpath, graph, visited)
                cpath.pop()
                if isLittle(n):
                    visited.remove(n)

crawler("start", path, graph, visited)

print(len(paths))