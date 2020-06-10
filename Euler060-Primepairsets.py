from sympy.ntheory import isprime
from math import floor, log10

def primesto(n):
    primes = []
    isprime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if isprime[p]:
            for i in range(2*p, n+1, p):
                isprime[i] = False
        p+=1
    isprime[0] = False
    isprime[1] = False
    isprime[2] = False
    isprime[5] = False
    for i, j in enumerate(isprime):
        if j:
            primes.append(i)
    return(primes)

def combo(a, b):
    return(isprime(int(a*(10**(floor(log10(b))+1))+b)) and isprime(int(b*(10**(floor(log10(a))+1))+a)))

def primepairs():
    primes = primesto(10000)
    for i in primes:
        for j in primes:
            if j < i:
                continue
            if combo(i, j):
                for k in primes:
                    if k < j:
                        continue
                    if combo(i, k) and combo(j, k):
                        for l in primes:
                            if l < k:
                                continue
                            if combo(i, l) and combo(j, l) and combo(k, l):
                                for m in primes:
                                    if m < l:
                                        continue
                                    if combo(i, m) and combo(j, m) and combo(k, m) and combo(l, m):
                                        return(i+j+k+l+m)

print(primepairs())
