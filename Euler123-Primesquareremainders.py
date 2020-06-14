from sympy.ntheory import primerange
def remainder(n, l):
    for i, j in enumerate(primerange(1, 10**l)):
        if (((j-1)**(i+1))+((j+1)**(i+1))) % (j**2) > 10**n:
            print(i+1)
            break

remainder(10, 6)
