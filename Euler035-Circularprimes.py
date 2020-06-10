def circularprimes(n):
    isprime = [True]*(n+1)
    a = 2
    primes = []
    c = 1
    p = 0
    while a*a <= n:
        if isprime[a]:
            for i in range(2*a, n+1, a):
                isprime[i] = False
        a+=1
    for i, j in enumerate(isprime):
        if j:
            primes.append(i)
    for i in primes:
        pc = True
        for j in str(i):
            if j in "024685":
                pc = False
                break
        if pc:
            isc = True
            s = [j for j in str(i)]
            for k in range(len(str(i))-1):
                p = s[0]
                del s[0]
                s.append(p)
                if not isprime[int("".join(s))]:
                    isc = False
                    break
            if isc:
                c +=1
    print(c)

circularprimes(1000000)
