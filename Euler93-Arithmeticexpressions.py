from itertools import product, permutations, combinations
from operator import add, sub, mul, truediv

def arith():
    t = 0
    s = 0
    for i in combinations(range(1, 10), 4):
        a = []
        for j in permutations(i):
            for k in product([add, mul, sub, truediv], repeat=3):
                b = k[0](k[1](j[0],j[1]),k[2](j[2], j[3]))
                if b == int(b) and b > 0 and int(b) not in a:
                    a.append(int(b))
                b = k[0](k[1](k[2](j[0],j[1]),j[2]),j[3])
                if b == int(b) and b > 0 and int(b) not in a:
                    a.append(int(b))
        a.sort()
        j = 0
        print(a)
        while a[j] == j+1:
            j+=1
            print(j)
        if j > s:
            s = j
            t = i
    print(t)

arith()
