from itertools import combinations
def lagrange(n):
    t = 0
    x = [i[0] for i in n]
    y = [i[1] for i in n]
    l = len(n)
    a = l+1
    for i, j in enumerate(combinations(x, l-1)):
        b = 1
        c = 1
        for k in j:
            b *= (a-k)
            c *= ((l-i)-k)
        t += ((b/c)*y[l-1-i])
    return(int(t))

def optimum():
    t = 1
    l = [(1, 1)]
    for i in range(2, 11):
        l.append((i, 1-i+(i**2)-(i**3)+(i**4)-(i**5)+(i**6)-(i**7)+(i**8)-(i**9)+(i**10)))
        t+=lagrange(l)
    print(t)

optimum()
