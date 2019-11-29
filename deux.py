import numpy as np
import copy

#----------------------init everything-------------------------
file = open('test2.txt', 'r')

adjMatrix = []
for line in file:
    adjMatrix.append(list(map(int, line.strip().split())))

adjMatrix = np.array(adjMatrix)
#--------------------------------------------------------------

class point():
    def __init__(self, id, edges):
        self.id = id
        self.edges = edges
        self.visited = False

class edge():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

points = []
allEdges = []
edges = []
for i in range(1, len(adjMatrix)+1):
    for j in range(1, len(adjMatrix)+1):
        if adjMatrix[i-1][j-1] == 1:
            if j>i:
                allEdges.append(edge(i, j))
            edges.append(edge(i, j))
    points.append(point(i, copy.deepcopy(edges)))
    edges.clear()

def val(point):
    return len(point.edges)

points.sort(key=val, reverse=True)

for p in points:
    if not p.visited:
        for e in p.edges:
            idd = e.p2
            for p2 in points:
                if idd == p2.id and not p2.visited:
                    for ee in allEdges:
                        if ee.visited == False and (p.id == ee.p1 and p2.id == ee.p2) or (p2.id == ee.p1 and p.id == ee.p2):
                            ee.visited = True
                            p.visited = True

ans = []
for p in points:
    if p.visited:
        ans.append(p.id)
print(f'{ans}\nVertex number : {len(ans)}')
