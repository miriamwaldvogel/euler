def prime(n):
    t = 0
    isprime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if isprime[p]:
            for i in range(2*p, n+1, p):
                isprime[i] = False
        p+=1
    isprime[0] = False
    isprime[1] = False
    for i in range(1, 577):
        if isprime[((i+1)**3)-(i**3)]:
            t += 1
    print(t)

prime(1000000)
