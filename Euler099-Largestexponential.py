from math import log10
f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p099_base_exp.txt', 'r')
g = f.readlines()
f.close()
h = []
m = 0
l = 0
for i in g:
    i = i[:-1].split(',')
    h.append((int(i[0]), int(i[1])))

for i, j in enumerate(h):
    if j[1]*log10(j[0]) > m:
        m = j[1]*log10(j[0])
        l = i+1
print(l)
