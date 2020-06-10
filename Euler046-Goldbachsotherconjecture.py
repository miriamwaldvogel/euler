from sympy.ntheory import isprime
from math import sqrt

def goldbach():
    i = 3
    p = [2]
    n = 0
    while n == 0:
        if isprime(i):
            p.append(i)
        else:
            a = True
            for j in p:
                if sqrt(((i-j)/2)) == int(sqrt(((i-j)/2))):
                    a = False
                    break
            if a:
                n = i
                print(n)
                break
        i+=2

goldbach()
