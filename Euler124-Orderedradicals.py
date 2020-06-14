def radicalsto(l, n):
    r = [[1, i] for i in range(l+1)]
    isprime = [True]*(l+1)
    p = 2
    while p*p <= l:
        if isprime[p]:
            for i in range(2*p, l+1, p):
                isprime[i] = False
        p+=1
    isprime[0] = False
    isprime[1] = False
    for i, j in enumerate(isprime):
        if j:
            for k in range(i, l+1, i):
                r[k][0] *= i
    print(sorted(r)[n][1])


radicalsto(100000, 10000)
