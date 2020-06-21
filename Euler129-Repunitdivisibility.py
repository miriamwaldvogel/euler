from sympy.ntheory import isprime

def divisibility(n):
    if isprime(n) or n % 5 == 0:
        return(1)
    i = 1
    a = 1
    while a != 0:
        a = (a*10+1)%n
        i += 1
    return(i)

def driver(n):
    i = 1000001
    while divisibility(i) < n:
        i += 2
    print(i)

driver(1000000)
