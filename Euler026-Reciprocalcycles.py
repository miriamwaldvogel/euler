def cycle(n):
    l = 1
    a = 1
    k = 1
    nines = int('9'*k)
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
    isprime[2] = False
    isprime[5] = False
    for i, j in enumerate(isprime):
        if j:
            primes.append(i)
    for i in primes:
        while nines % i != 0:
            k +=1
            nines = int('9'*k)
        if k > l:
            l = k
            a = i
        k = 1
    print(a)

cycle(1000)
