from math import log, factorial

def fives(n):
    if n == 0:
        return(0)
    return(sum(int(n/(5**i)) for i in range(1, int(log(n, 5))+1)))

def twos(n):
    if n == 0:
        return(0)
    return(sum(int(n/(2**i)) for i in range(1, int(log(n, 2))+1)))

def choose(a, b):
    f = 1
    for i in range(b+1, a+1):
        f *= i
    return(int(f/factorial(a-b)))

def pascal(n, p):
    a = twos(n)
    b = fives(n)
    t = 0
    d = 0
    for i in range(n, -1, -1):
        e = int(i/2)
        c = min([a-sum([twos(e), twos(i-e), twos(n-i)]), b-sum([fives(e), fives(i-e), fives(n-i)])])
        if c >= p:
            t += 1
            if i % 2 == 0:
                d += 1
        for j in range(int(i/2)-1, -1, -1):
            w = [twos(j), twos(i-j), twos(n-i)]
            f = [fives(j), fives(i-j), fives(n-i)]
            c = min([a-sum(w), b-sum(f)])
            if c >= p:
                t += 1
            """if w[0]+w[2] >= a-p or f[0]+f[2] >= a-p:
                break"""
    print(2*t-d, t, d)

def pyramid(n):
    r = [choose(n, i) for i in range(n+1)]
    t = 0
    for i in range(n):
        for j in range(i+1):
            if (choose(i, j)*r[i]) % 10 == 0:
                t += 1
    for i in r:
        if i % 10 == 0:
            t += 1
    print(t)

n = 57
pascal(n, 1)
pyramid(n)
