def primesum(n):
    primes = []
    isprime = [True]*(n+1)
    p = 2
    b = 0
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
    for i in range(len(primes)-2):
        t = 0
        a = i
        c = 0
        if i != 0:
            t += primes[a]
            a+=1
            c+=1
        while a+1 < len(primes) and t+primes[a]+primes[a+1]<n:
            t += primes[a]+primes[a+1]
            a+=2
            c+=2
            if b <= c and isprime[t]:
                r = t
                b = c
    print(r)

primesum(1000000)
