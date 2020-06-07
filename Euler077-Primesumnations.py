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

def primesums(n):
    primes = primesto(80)
    i = 11
    t = [1]+([0]*i)
    while t[i-1] < n:
        t = [1]+[0]*i
        for j in primes:
            for k in range(j, i+1):
                t[k]+=t[k-j]
        i+=1
    print(i-1)

primesums(5000)
