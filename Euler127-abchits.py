from math import ceil
def product(n):
    p = 1
    for i in n:
        p *= i
    return(p)

def hits(n):
    f = [[] for i in range(n+1)]
    r = [1]*(n+1)
    isprime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if isprime[p]:
            for i in range(2*p, n+1, p):
                isprime[i] = False
        p+=1
    isprime[0] = False
    isprime[1] = False
    for i in range(2, n+1, 2):
        f[i].append(2)
        r[i] *= 2
    composite = []
    for i in range(3, n+1):
        if isprime[i]:
            for j in range(i, n+1, i):
                f[j].append(i)
                r[j] *= i
        else:
            composite.append(i)
    t = 0
    for i in composite:
            if r[i]*6 <= i:
                b = ceil(i/2)
                a = [True]*(b+1)
                for j in f[i]:
                    for k in range(j, b+1, j):
                        a[k] = False
                for j, k in enumerate(a):
                    if k:
                        c = i-j
                        if r[i]*r[j]*r[c] < i and len(set(f[i]+f[j]+f[c])) == len(f[i])+len(f[j])+len(f[c]):
                            t += i
                        #t += 1
            else:
                d = i-1
                e = i-d
                if r[i]*r[d]*r[e] < i and len(set(f[i]+f[d]+f[e])) == len(f[i])+len(f[d])+len(f[e]):
                    t += i

    print(t)
hits(120000)
