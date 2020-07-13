s = []
a = [((100003 - 200003*i + 300007*i*i*i)%1000000)-500000 for i in range(1, 56)]
for i in range(56, 2001):
    a.append(((a[i-25]+a[i-56]+1000000)%1000000)-500000)
s.append(a)
c = a + []
s += [[] for i in range(1999)]
for i in range(1, 2000):
    for j in range(1, 2001):
        b = i*2000+j
        c.append(((c[b-25]+c[b-56]+1000000)%1000000)-500000)
        s[i].append(c[-1])

def subsum(x, y, a, b):
    global s
    r = 0
    i = 0
    while 0 <= x < 2000 and 0 <= y < 2000:
        i = max(i+s[y][x], 0)
        r = max(i, r)
        x += a
        y += b
    return(r)

print(max(max(subsum(0, i, 1, 0), subsum(i, 0, 0, 1), subsum(0, i, 1, 1), subsum(i, 0, 1, 1), subsum(i, 0, -1, 1), subsum(1999, i, -1, 1)) for i in range(2000)))
