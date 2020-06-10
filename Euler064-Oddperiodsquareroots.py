from math import sqrt

def period(n):
    t = 0
    for i in range(2, n+1):
        r = int(sqrt(i))
        l = int(sqrt(i))
        if l**2 == i:
            continue
        k = 1
        p = 0
        while k !=1 or p == 0:
            k = int((i-r*r)/k)
            r = int((l + r)/k)*k-r
            p += 1
        if p % 2 == 1: t += 1
    print(t)

period(10000)
