from sympy.ntheory import isprime

def maxtotientratio(n):
    t = 1
    c = 2
    while t*c < n:
        if isprime(c):
            t *= c
        c += 1
    print(t)

maxtotientratio(1000000)
