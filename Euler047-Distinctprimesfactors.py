isprime = []
primes = []

def primesto(n):
    global isprime, primes
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

def fourfactors(n):
    global isprime, primes
    f = 0
    i = 0
    while primes[i] <= int(n/2):
        if n % primes[i] == 0:
            f += 1
            if f > 3:
                return(True)
                break
        i+=1
    return(False)

def driver(n):
    global isprime, primes
    primesto(n)
    a = 0
    i = 130000
    f = [False]*(n+1)
    f[210] = True
    while a == 0 and i < n:
        if not isprime[i]:
            f[i] = fourfactors(i)
            if f[i] and f[i-1] and f[i-2] and f[i-3]:
                a = i-3
                print(a)
                break
        #print(i)
        i+=1

driver(150000)
