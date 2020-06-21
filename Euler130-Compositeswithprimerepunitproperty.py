from sympy.ntheory import isprime
def a(n):
    i = 1
    a = 1
    while a != 0:
        a = (a*10+1)%n
        i += 1
    return(i)

def composites(n):
    c = 0
    t = 0
    i = 9
    while c < n:
        if not isprime(i) and i % 5 != 0 and (i-1)%a(i) == 0:
            c += 1
            t += i
        i += 2
    print(t)

composites(25)
#print(a(41))
