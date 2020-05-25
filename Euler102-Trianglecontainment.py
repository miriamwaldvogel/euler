f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p102_triangles.txt', 'r')
g = f.read().split('\n')
f.close()
t = 0
def area(n):
    return(abs((n[0]*(n[3]-n[5])+n[2]*(n[5]-n[1])+n[4]*(n[1]-n[3]))/2))

for i in range(len(g)-1):
    a = [int(j) for j in g[i].split(',')]
    if area(a) == area([0, 0, a[0], a[1], a[2], a[3]])+area([0, 0, a[0], a[1], a[4], a[5]])+area([0, 0, a[2], a[3], a[4], a[5]]):
        t+=1
print(t)
