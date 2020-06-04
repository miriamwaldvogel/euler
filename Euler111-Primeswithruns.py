from itertools import combinations, product
from sympy.ntheory import isprime
def run(l, r, t):
    p = 0
    for i in combinations(range(t), l):
        a = []
        b = [0 for i in range(t)]
        for j in range(t):
            if j not in i:
                a.append(j)
            else:
                b[j] = r
        for j in product(range(10), repeat=t-l):
            for k, m in enumerate(j):
                b[a[k]] = m
            c = int("".join([str(o) for o in b]))
            if c >= 10**(t-1) and isprime(c):
                p += c
    return(p)

def driver(n):
    t = 0
    for i in range(10):
        j = n-1
        a = run(j, i, n)
        while a == 0:
            j-=1
            a = run(j, i, n)
        t+=a
    print(t)

driver(10)
