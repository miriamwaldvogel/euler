from re import split
import networkx as nx
f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p081_matrix.txt', 'r')
g = split(',|\n', f.read())
f.close()
h = []
d = 80
for i in range(d):
    a = []
    for j in range(d):
        a.append(int(g[(i*d)+j]))
    h.append(a)

g = nx.DiGraph()
for i in range(d):
    for j in range(d):
        b = [(i+x, j+y) for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)) if 0 <= i+x < d and 0 <= j+y < d]
        for c, e in b:
            g.add_edge((i, j), (c, e), weight = h[c][e])
print(nx.dijkstra_path_length(g, source=(0, 0), target=(d-1, d-1))+h[0][0])
