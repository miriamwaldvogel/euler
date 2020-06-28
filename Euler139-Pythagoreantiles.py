def newmatrice(a):
    return([abs(sum(k*a[j] for j, k in enumerate(i))) for i in [(1, 2, 2), (2, 1, 2), (2, 2, 3)]])

def triples(n):
    s = [[3, 4, 5]]
    b = 0
    t = int(n/12)
    while b < n:
        a = []
        for i in s:
            j = sorted(newmatrice(i))
            b = sum(j)
            if b <= n:
                a.append(j)
                if pow(j[2], j[2], (j[1]-j[0])**2) == 0:
                    t += int(n/b)
        s = a
    print(t)

triples(100000000)
