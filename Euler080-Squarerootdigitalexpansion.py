from math import sqrt
def rootdigits(n):
    c = int(sqrt(n))
    t = c
    s = c
    b = c**2
    a = n
    for i in range(99):
        a-=b
        a*= 100
        c+=s
        j = 1
        while ((c*10)+j)*j <= a:
            j+=1
        j-=1
        s = j
        c*= 10
        c+=j
        b = c*j
        t+=s
    return(t)

def driver(n):
    t = 0
    for i in range(2, n+1):
        if sqrt(i) != int(sqrt(i)):
            t+=rootdigits(i)
    print(t)

driver(100)
