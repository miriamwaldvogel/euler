from sympy.ntheory import isprime
def tile(n, s):
    a = 2
    b = 2
    t = []
    for i in range(1, n):
        c = b
        b = a
        a += 6*i
        if sum(1 for j in [1+6*i, 6*(i+1)+a-1-b, a-1-b, b-c] if isprime(j)) == 3:
            t.append(b)
        if sum(1 for j in [a-b-1, a-c-1, a-b, 1+6*(i+1)-2] if isprime(j)) == 3:
            t.append(a-1)
        if len(t) >= s:
            return(t[s-1])
    return(len(t))

print(tile(100000, 2000))
