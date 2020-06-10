from math import sqrt
def sumdivisors(n):
    d = 1
    s = sqrt(n)
    for i in range(2, int(s)+1):
        if n % i == 0:
            d += i+int(n/i)
    if s == int(s):
        d -= int(s)
    return(d)

def abundant(n):
    t = 0
    a = set()
    for i in range(1, n):
        if sumdivisors(i) > i:
            a.add(i)
        if not any(i-j in a for j in a):
            t += i
    print(t)

abundant(28213)
