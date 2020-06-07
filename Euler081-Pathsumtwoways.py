from re import split
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

t = list(h)
for i in range(1, d):
    t[0][i]+=t[0][i-1]
    t[i][0]+=t[i-1][0]
for i in range(1, d):
    for j in range(1, d):
        t[i][j]+=min(t[i-1][j], t[i][j-1])
print(t[d-1][d-1])
