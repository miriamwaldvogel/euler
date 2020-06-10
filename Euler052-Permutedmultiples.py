from math import log

def permutedmultiples(a):
    n = 0
    c = 125874
    while n == 0:
        if a*c <= int(log(c, 10))**10:
            s = True
            t = sorted([i for i in str(c)])
            for i in range(2, a+1):
                if sorted([i for i in str(i*c)]) != t:
                    s = False
                    break
            if s:
                n = c
                print(n)
        c+=1

permutedmultiples(6)
