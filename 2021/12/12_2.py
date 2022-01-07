FILE = "input.txt"

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


paths = set()
path = ["start"]
visited = {"start"}


def crawler(node, cpath, graph, visited, doublePresent):
    if node == "end":
        paths.add(tuple(cpath))
        return
    else:
        for n in graph[node]:
            if n not in visited:
                cpath.append(n)
                if isLittle(n):
                    visited.add(n)
                crawler(n, cpath, graph, visited, doublePresent)
                if isLittle(n):
                    visited.remove(n)
                if not doublePresent and isLittle(n):
                    crawler(n, cpath, graph, visited, True)
                cpath.pop()


crawler("start", path, graph, visited, False)

print(len(paths))
