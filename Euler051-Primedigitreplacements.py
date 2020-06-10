def primedigitreplacements(n, l):
    isprime = [True] * (l+1)
    p = 2
    primes = []
    while p * p <= l:
        if isprime[p]:
          for i in range(2*p, l+1, p):
            isprime[i] = False
        p+=1
    isprime[0] = False
    isprime[1] = False
    for i, j in enumerate(isprime):
        if j:
            primes.append(i)
            s = str(i)
            d = 0
            c = 1
            if '0' in s:
                d = 1
            elif '1' in s:
                d = 2
            elif '2' in s:
                d = 3
            if d > 0 and i > 10:
                for l in range(d, 10):
                    t = ''
                    for m in s:
                        b = m
                        if m == str(d-1):
                            b = str(l)
                        t += b
                    if isprime[int(t)]:
                        c+=1
                        if c >= n:
                            return(i)
                            break

print(primedigitreplacements(8, 1000000))
