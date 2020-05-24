from math import sqrt
isprime = []

def isprime(n):
    isprime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if isprime[p]:
            for i in range(2*p, n+1, p):
                isprime[i] = False
        p+=1
    isprime[0] = False
    isprime[1] = False
    return(isprime)

def amicable(n):
    t = 1
    s = sqrt(n)
    for i in range(2, int(s)):
        if n % i == 0:
            t += i
            t += int((n/i))
    if s == int(s):
        t += int(s)
    return(t)

def driver(n):
    prime = isprime(n)
    m = 0
    l = 0
    for i in range(2, n):
        if not prime[i]:
            j = 0
            a = amicable(i)
            b = [i]
            while a < n and not prime[a] and a != i and a not in b:
                b.append(a)
                a = amicable(a)
                j+=1
            if a < n and not prime[a]:
                if a == i:
                    if len(b) > 0:
                        j+=1
                        if j > l:
                            l = j
                            m = min(b)
                else:
                    c = b.index(a)
                    if j-c > l:
                        l = j-c
                        m = min(b[c:])
    print(m)

driver(1000000)
