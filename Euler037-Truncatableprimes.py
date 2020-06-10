primes = []
isprime = []
def primesto(n):
    global primes, isprime
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
primesto(999999)
def truncatable():
    global isprime, primes
    t = 0
    a = 4
    while a < len(primes):
        ist = True
        s = str(primes[a])
        for i in range(len(s), 0, -1):
            if not isprime[int(s[:i])] or not isprime[int(s[len(s)-i:len(s)])]:
                ist = False
                break
        if ist:
            t += primes[a]
        a+=1
    print(t)

truncatable()
