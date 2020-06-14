from math import sqrt

def sums(n):
    t = set()
    for i in range(1, int(sqrt(n/2))):
        a = i**2
        for j in range(i+1, int(sqrt(n/2))+1):
            a += j**2
            if a > n:
                break
            if str(a) == str(a)[::-1]:
                t.add(a)
    print(sum(t))
sums(100000000)
