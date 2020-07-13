from sympy.ntheory import isprime

def pattern(n):
    l = int(n/10)
    p = [3, 7, 13]
    a = [1]*(l+1)
    t = 0
    for i in p:
        for j in range(i, l+1, i):
            a[j] = 0
    for i, j in enumerate(a):
        if j == 1:
            if pow(i*10, i*10, 6) == 4:
                c = i*i*10*10
                if not isprime(c+19) and not isprime(c+21) and isprime(c+1) and isprime(c+3) and isprime(c+7) and isprime(c+9) and isprime(c+13) and isprime(c+27):
                    print(i*10)
                    t += i*10
    print(t)

pattern(150000000)
