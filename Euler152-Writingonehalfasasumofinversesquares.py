from itertools import combinations
from math import ceil

def inverse():
    s = [4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18, 20, 21, 24, 28, 30, 35, 36, 39, 40, 42, 45, 52, 56, 60, 63, 70, 72]
    a = [int(1073217600/(i**2)) for i in s]
    b = sum(a)
    t = 0
    d = 149058000
    for i in range(5, ceil(len(a)/2)):
        for j in combinations(a, i):
            c = sum(j)
            if c == d:
                t += 1
            elif b-c == d:
                t += 1
    for i in range(1, 5):
        for j in combinations(a, i):
            if b-sum(j) == d:
                t += 1
    print(t)

inverse()
