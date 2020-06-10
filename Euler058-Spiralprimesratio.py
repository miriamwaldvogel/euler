from sympy.ntheory import isprime

def spiral():
    a = 4
    d = [3, 5, 7, 9]
    p = 3
    b = 5
    while float(p)/b > 0.1:
        d[0] = d[3]+a
        for i in range(1, 4):
            d[i] = d[i-1]+a
            if isprime(d[i]):
                p += 1
        if isprime(d[0]):
            p += 1
        a += 2
        b += 4
    print(a-1)


spiral()
