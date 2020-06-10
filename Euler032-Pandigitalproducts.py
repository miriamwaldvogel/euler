from math import floor

def pandigital():
    p = set()
    d = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(2, 100):
        for j in range(101, floor(9876/i)+1):
            a = i*j
            b = sorted([i for i in str(i)+str(j)+str(a)])
            if b == d:
                p.add(a)
    print(sum(p))

pandigital()
