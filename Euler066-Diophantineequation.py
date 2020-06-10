from math import sqrt
def period(n):
    s = sqrt(n)
    p = int(s)
    q = p
    a = 0
    m = 0
    d = 1
    l = []
    while q != (2*p):
        m = d*q - m
        d = (n - m**2)/d
        q = int((p+m)/d)
        a+=1
        l.append(q)
    return(l)

def minsolution(n):
    p = period(n)
    n1 = int(sqrt(n))
    n2 = (n1*p[0])+1
    d1 = 1
    d2 = p[0]
    i = 1
    if (n1**2) - ((d1**2)*n) == 1:
        return(n1)
    else:
        while (n2**2) - ((d2**2)*n) != 1:
            c = n1
            n1 = n2
            n2 *= p[i%len(p)]
            n2 += c
            c = d1
            d1 = d2
            d2 *= p[i%len(p)]
            d2 += c
            i+=1
        return(n2)

def maxsolution(n):
    m = 0
    a = 0
    for i in range(2, n+1):
        if sqrt(i) != int(sqrt(i)):
            a = minsolution(i)
            if m < a:
                m = a
                d = i
    print(d)

maxsolution(1000)
