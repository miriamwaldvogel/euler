from networkx import find_cycle, DiGraph
f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p107_network.txt', 'r')
b = set()
for i, j in enumerate(f):
    a = j.replace('\n', '').split(',')
    for k, l in enumerate(a):
        if l != '-':
            b.add((int(l), (min(i, k), max(i, k))))
f.close()
b = list(b)
c = [i[0] for i in b]
d = sorted(c)
t = -8
e = []
i = 0
while len(e) < 40:
    e.append(b[c.index(d[i])])
    try:
        find_cycle(DiGraph(e), orientation='ignore')
        del e[-1]
    except:
        t+=d[i]
    i+=1
print(sum(d)-t)
