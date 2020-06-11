from itertools import permutations
from sympy.ntheory import isprime
s = []
def sums(l, i, n, r):
    global s
    if r < 0:
        return
    if r == 0:
        s.append(l[:i])
        return
    if i == 0:
        p = 1
    else:
        p = l[i-1]
    for k in range(p, n + 1):
        l[i] = k
        sums(l, i + 1, n, r - k)

def primesets():
    global s
    sums([0]*9, 0, 9, 9)
    d = {}
    for i in filter(lambda x: x[8]%2 == 1, permutations(range(1, 10), 9)):
        for j in s:
            a = 0
            c = True
            b = []
            for k in j:
                b.append(sum(m * (10**(k-l-1))for l, m in enumerate(i[a:a+k])))
                if not isprime(b[-1]):
                    c = False
                    break
                a += k
            if c:
                d[tuple(sorted(b))] = 1
    print(len(d))

primesets()
