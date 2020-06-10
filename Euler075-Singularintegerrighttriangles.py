def newmatrice(a, b):
    return([abs(sum(k*a[j] for j, k in enumerate(i))) for i in b])

def newtriples(n):
    m = [[(-1, 2, 2), (-2, 1, 2), (-2, 2, 3)], [(1, 2, 2), (2, 1, 2), (2, 2, 3)], [(1, -2, 2), (2, -1, 2), (2, -2, 3)]]
    return([newmatrice(n, i) for i in m])

def gentriples(n):
    s = [[3, 4, 5]]
    t = []
    f = 0
    d = [0]*(n+1)
    b = 0
    for i in range(12, n+1, 12):
        d[i] += 1
    while b < n:
        a = []
        for i in s:
            t.append(i)
            for j in newtriples(i):
                b = sum(j)
                if b <= n:
                    a.append(j)
                    if d[b] < 2:
                        for k in range(b, n+1, b):
                            d[k]+=1
        s = a
    for i in d:
        if i == 1:
            f += 1
    print(f)

gentriples(1500000)
