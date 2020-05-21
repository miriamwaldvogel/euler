def primesto(n):
    isprime = [True]*(n+1)
    p = 2
    primes = []
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

def primetriples(n):
    p = primesto(7080)
    triple = [0 for i in range(n+1)]
    i = 0
    while p[i] ** 4 < n:
        j = 0
        while p[j] ** 3 < n - (p[i]**4):
            k = 0
            while p[k] ** 2 < n - (p[i]**4) - (p[j]**3):
                triple[(p[i]**4)+(p[j]**3)+(p[k]**2)] = 1
                k +=1
            j += 1
        i+=1
    print(sum(triple))

primetriples(50000000)
