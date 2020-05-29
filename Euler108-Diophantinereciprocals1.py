from math import log
def s(n):
    return((2*n)+1)
def reciprocals(n):
    h = 510510
    t = []
    for i in range(5):
        a = 17**i
        for j in range(int(log(h/a, 13))+1):
            b = 13**j
            for k in range(int(log(h/(a*b), 11))+1):
                c = 11**k
                for l in range(int(log(h/(a*b*c), 7))+1):
                    d = 7**l
                    for m in range(int(log(h/(a*b*c*d), 5))+1):
                        e = 5**m
                        for o in range(int(log(h/(a*b*c*d*e), 3))+1):
                            f = 3**o
                            for p in range(int(log(h/(a*b*c*d*e*f), 2))+1):
                                if ((s(i)*s(j)*s(k)*s(l)*s(m)*s(o)*s(p))+1)/2 > n:
                                    t.append((a*b*c*d*e*f*(2**p)))
    print(min(t))


reciprocals(1000)
