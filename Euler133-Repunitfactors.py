def factors(n):
    isprime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if isprime[p]:
            for i in range(2*p, n+1, p):
                isprime[i] = False
        p+=1
    isprime[0] = False
    isprime[1] = False
    t = 5
    for i in range(3, n+1, 2):
        if isprime[i]:
            if pow(10, 10**20, i) != 1:
                t += i
    print(t)

factors(100000)
