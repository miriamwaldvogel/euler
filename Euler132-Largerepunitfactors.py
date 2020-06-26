from sympy.ntheory import isprime

def factors(n, f):
    t = 0
    i = 5
    a = 0
    while a < f:
        if isprime(i) and pow(10, 10**n, i) == 1:
            t += i
            a += 1
        i += 2

    print(t)

factors(9, 40)
