from math import gcd, sqrt
from sympy.ntheory import factorint, isprime, divisors

t = 0
g = []
def modify(i, j, n):
    global t
    a = i+j+i+j
    l = (i*j)/gcd(i, j)
    t += a*int(n/int((l*i)/j+(j*l)/i))
    #print(i, j, int(l), int((l*i)/j), int((j*l)/i), int((l*i)/j+(j*l)/i))
def series(a, b, s):
    return((s + b)*int(int(b/s)/2)-(s + a)*int(int(a/s)/2))
def gaussian(n):
    global t, g
    q = [1, 5, 4, 13, 12, 20, 8, 29, 13, 56, 12, 52, 24, 40, 48, 61, 28, 65, 20, 144, 32, 60, 24, 116, 81, 112, 40, 104, 44, 224, 32, 125, 48, 136, 96, 169, 52, 100, 96, 320, 60, 160, 44, 156, 156, 120, 48, 244, 57, 369, 112, 288, 72, 200, 144, 232, 80, 212, 60, 576, 84, 160, 104]
    v = [0, 0, 0]
    h = int(n/2)
    t += int(((n+1)*n)/2-(h*(h+1))/2)
    for i in range(1, h+1):
        t += 2*i*int(n/(2*i))+i*(int(n/i))
    for i in range(1, int(sqrt(n-1))+1):
            for j in range(1, i):
                modify(i, j, n)
    v[0] = t
    print('-------------------------------------------------------------------------')
    for i in range(int(sqrt(n-1))+1, int(n/4)):
        if not isprime(i):
            f = [False]*i
            for j in factorint(i):
                for k in range(j, i, j):
                    f[k] = True
            for j, k in enumerate(f):
                if k:
                    modify(i, j, n)
    print('-------------------------------------------------------------------------')
    v[1] = t-v[0]
    for i in range(int(n/4), 2*int(n/5)+1):
        if not isprime(i):
            for j in divisors(i)[-2::-1]:
                if i*i/j+j > n:
                    break
                t += 2*(i+j)*int(n/((i*i)/j+j))
    v[2] = t-v[1]-v[0]
    #print(sum(q[:n]))
    print(t)
    print(v)

gaussian(1000)
