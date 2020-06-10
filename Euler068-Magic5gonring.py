from itertools import permutations

def shift(n):
    a = sorted(n)
    while n[0] != a[0]:
        b = n[0]
        n[0] = n[1]
        n[1] = n[2]
        n[2] = n[3]
        n[3] = n[4]
        n[4] = b
    return(n)

def posring(n):
    return(any(n[i] == 10 for i in (0, 6, 7, 8, 9)) and n[0]+n[1]+n[3] == n[6]+n[3]+n[5] == n[7]+n[5]+n[4] == n[8]+n[4]+n[2] == n[9]+n[2]+n[1])

def ring():
    p = filter(posring, permutations(range(1, 11), 10))
    a = []
    for i in p:
        b = shift([(i[0], i[1], i[3]), (i[6], i[3], i[5]), (i[7], i[5], i[4]), (i[8], i[4], i[2]), (i[9], i[2], i[1])])
        if a < b:
            a = b
    s = ''
    for i in a:
        for j in i:
            s += str(j)
    print(s)

ring()
