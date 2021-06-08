import networkx
import math
from prettytable import PrettyTable as table

g = networkx.Graph()
for i in "xzyvtuw":
    g.add_node(i)
g.add_weighted_edges_from([("z", "y", 12), ("z", "x", 8), ("x", "y", 6), ("x", "v", 3), ("x", "w", 6), ("y", "v", 8),
                           ("y", "t", 7), ("v", "t", 4), ("v", "w", 4), ("v", "u", 3), ("w", "u", 3), ("u", "t", 2)])


def djkesrtra(gr, n, t):
    d = dict()
    for i in g.nodes:
        d[i] = [False, math.inf, None]
    d[n] = [True, 0, None]
    s = 1
    while s < len(d):
        smallest = [None, math.inf]
        for i in gr[n].keys():
            if not d[i][0] and d[i][1] > gr[n][i]["weight"] + d[n][1]:
                d[i] = [False, gr[n][i]["weight"] + d[n][1], n]
        for j, i in d.items():
            if i[1] < smallest[1] and not i[0]:
                smallest = [j, i[1]]
        k = [s]
        for i in d.keys():
            k.append(d[i][2:0:-1])
        t.add_row(k)
        d[smallest[0]][0] = True
        n = smallest[0]
        s += 1
    return d


def printRoute(d, x):
    while x is not None:
        print(x, end="<-")
        x = d[x][2]
    print()

for i in g.nodes:
    t = table(list("#" + "xzyvtuw"))
    t.title = i + "'s table"
    d = djkesrtra(g, i, t)

    print(t)
    print("Fastest Route")
    for i in g.nodes:
        printRoute(d, i)
