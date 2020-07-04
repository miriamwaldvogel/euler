from math import sqrt, gcd

def progressive(n):
    l = 10**n
    t = set()
    for i in range(2, 10**int(n/3)):
        for j in range(1, i):
            if i*i*i*j*j+(j**2) >= l:
                break
            if gcd(i, j) > 1:
                continue
            k = 1
            a = i*i*i*j*k*k+k*j*j
            while a <= l:
                if sqrt(a) == int(sqrt(a)):
                    t.add(a)
                k += 1
                a = i*i*i*j*k*k+k*j*j
    print(sum(t))

progressive(12)
