from math import sqrt

def cuboids(n):
    i = 0
    a = 2
    while i < n:
        a+=1
        for j in range(3, 2*a):
            if (j*a) % 12 == 0:
                b = sqrt((j**2)+(a**2))
                if b == int(b):
                    i += min(j, a+1) - float(j+1)/2
    print(a-2)

cuboids(1000000)
