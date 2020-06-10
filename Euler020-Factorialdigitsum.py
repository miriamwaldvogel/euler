from math import factorial

def factorialdigitsum(n):
    s = 0
    for i in str(factorial(n)):
        s += int(i)
    print(s)

factorialdigitsum(100)
