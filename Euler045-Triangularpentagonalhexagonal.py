from math import sqrt

def tph():
    h = 40755
    a = 143
    s = 0
    while s == 0:
        h += 1+(4*a)
        a+=1
        if (sqrt((24*h)+1)+1) % 6 == 0:
            s = h
    print(s)

tph()
