from math import floor

def trianglesolutions(n):
    s = 0
    for i in range(1, floor(n/3)):
        for j in range(i, n-i+1):
            if (i**2)+(j**2) == (n-i-j)**2:
                s+=1
    return(s)

def maxtriangles():
    n = 0
    p = 0
    a = 0
    for i in range(10, 1001, 10):
        a = trianglesolutions(i)
        if a > n:
            n = a
            p = i
    print(p)

maxtriangles()
