from fractions import gcd
def numtriangles(n):
    t = 0
    for i in range(1, n+1):
        for j in range(1, n):
            a = gcd(i, j)
            t += min(i*a/j, a*(n-j)/i)
    print((int(t)*2)+(n*n*3))

numtriangles(50)
