f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p067_triangle.txt', 'r')
g = f.readlines()
f.close()
h = []
b = []
for i in g:
    i = i[:-2].split(' ')
    for j in i:
        b.append(int(j))
    h.append(b)
    b = []
for i in range(len(h)-1, 0, -1):
    for j in range(0, i):
        h[i-1][j]+= max(h[i][j], h[i][j+1])
print(h[0][0])
