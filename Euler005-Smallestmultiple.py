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
    for i, j in enumerate(isprime):
        if j:
            primes.append(i)
    return(primes)

def smallestmultiple(n):
    p = primesto(n)
    d = [1]*(n+1)
    for i in range(2, n):
        for j in p:
            if j > i/2:
                break
            k = 0
            a = i
            while a % j == 0:
                a /= j
                k += 1
            if k > d[j]:
                d[j] = k
    t = 1
    for i in p:
        t *= i**d[i]
    print(t)

smallestmultiple(20)
