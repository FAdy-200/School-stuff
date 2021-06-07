import networkx
import math

g = networkx.DiGraph()
d = dict()
for i in "ABCDEFGH":
    g.add_node(i)
    d[i] = [False, math.inf, None]
g.add_weighted_edges_from([("A", "B", 2), ("A", "D", 4), ("A", "C", 1), ("B", "F", 2), ("B", "C", 5), ("B", "E", 10),
                           ("C", "A", 9), ("C", "E", 11), ("D", "C", 2), ("E", "D", 7), ("E", "G", 1), ("F", "H", 3),
                           ("H", "G", 1), ("G", "F", 2), ("G", "E", 3)])

print(g["B"])


def djkesrtra(gr, n, dist, d):
    d[n] = [True, 0, None]
    s = 1
    while s < len(d):
        smallest = [None, math.inf]
        for i in gr[n].keys():
            if not d[i][0]:
                d[i] = [False, gr[n][i]["weight"] + d[n][1], n]
        for j, i in d.items():
            if i[1] < smallest[1] and not i[0]:
                smallest = [j, i[1]]

        d[smallest[0]][0] = True
        n = smallest[0]
        s += 1


x = "E"
djkesrtra(g, "A", x, d)
print(d[x][1])
while x is not None:
    print(x, end="<-")
    x = d[x][2]
print(d)
