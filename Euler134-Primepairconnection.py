from math import log10
def congruence(a, b, m):
    if b == 0:
        return(0)
    if a < 0:
        a = -a
        b = -b
    b %= m
    while a > m:
        a -= m
    return(int((m*congruence(m, -b, a)+b)/a))
#print(congruence(100, 4, 23))
def primepair(n):
    isprime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if isprime[p]:
            for i in range(2*p, n+1, p):
                isprime[i] = False
        p+=1
    isprime[0] = False
    isprime[1] = False
    q = 5
    t = 0
    for i in range(7, n+1, 2):
        if isprime[i]:
            a = 10**(int(log10(q))+1)
            t += congruence(a, i-q, i)*a+q
            q = i
    print(t)

primepair(1000004)
