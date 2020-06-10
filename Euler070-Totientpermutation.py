from sympy.ntheory import primerange
from math import sqrt
def permutation(a, b):
    return(sorted([i for i in str(a)]) == sorted([i for i in str(b)]))

def totient(n):
    q = 2
    a = 0
    i = 0
    p = list(primerange(2, int(1.2*sqrt(n))))
    del p[:int(0.6*len(p))]
    for j in p:
        i += 1
        for k in p[i:]:
            if (j+k) % 9 != 1:
                continue
            b = j*k
            if b > n:
                return(a)
            t = (j-1)*(k-1)
            c = b/float(t)
            if permutation(t, b) and q > c:
                q = c
                a = b

print(totient(10000000))
