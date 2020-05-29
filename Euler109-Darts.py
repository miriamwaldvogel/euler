def checkout(n):
    w = 0
    double = [2*i for i in range(1, 21)]+[50]
    total = sorted(double+[i for i in range(1, 21)]+[3*i for i in range(1, 21)]+[25])
    e = 0
    for i in double:
        if i == n:
            w+=1
            break
        a = n-i
        for j, k in enumerate(total):
            if k == a:
                w+=1
            elif k > a:
                break
            b = a-k
            for l, m in enumerate(total):
                if m == b:
                    w+=1
                    if j != l:
                        e+=1
    w-=int(e/2)

    return(w)

def darts(n):
    t = 0
    for i in range(1, n):
        t+=checkout(i)
    print(t)

darts(100)
