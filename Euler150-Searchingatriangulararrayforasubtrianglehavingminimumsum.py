s = []
c = 0
a = 2**19
b = 2**20
for i in range(1, 500501):
    c = (615949*c+797807)%(b)
    s.append(c-a)
d = 0
t = []
for i in range(1, 1001):
    t.append(s[d:d+i])
    d += i

def minsum(n):
    r = 0
    d = len(n)
    for i in range(d):
        for j in range(i+1):
            a = n[i][j]
            for k in range(1, d-i):
                a += sum(n[i+k][j:j+k+1])
                r = min(a, r)
    print(r)

minsum(t)
