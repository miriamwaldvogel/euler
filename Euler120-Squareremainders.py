from math import ceil

def remainder(n):
    print(sum((ceil(i/2)-1)*2*i for i in range(3, n+1)))

remainder(1000)
