def quadraticprimes(n):
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
    a = 0
    c = 0
    d = 0
    s = [i*-1 for i in primes[:168]]
    p = 0
    for i in s:
        for j in primes[:168]:
            while isprime[a**2+(i*a)+j]:
                c+=1
                a+=1
            if c > d:
                d = c
                p = i*j
            c = 0
            a = 0
    print(p)

quadraticprimes(14803)
