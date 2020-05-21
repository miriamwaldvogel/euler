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
c = [h[i][-1] for i in range(d)]

for i in range(d-2, -1, -1):
	c[0] += h[0][i]
	for j in range(1, d):
		c[j] = min(c[j], c[j-1]) + h[j][i]
	for j in range(d-2, -1, -1):
		c[j] = min(c[j], c[j+1] + h[j][i])
print(min(c))
