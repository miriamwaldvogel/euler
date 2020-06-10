from math import sqrt
def sumdivisors(n):
    d = 1
    s = sqrt(n)
    for i in range(2, int(s)):
        if n % i == 0:
            d += i+int(n/i)
    if s == int(s):
        d += int(s)
    return(d)

def amicable(n):
    t = 0
    for i in range(2, n):
        a = sumdivisors(i)
        b = sumdivisors(a)
        if b == i and a != b:
            t += a+b
    print(int(t/2)-1)

amicable(10000)
