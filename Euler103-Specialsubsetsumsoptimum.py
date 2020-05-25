from itertools import combinations

def special(n):
    for i in range(1, int(len(n)/2)+1):
        for j in range(i, len(n)-i+1):
            for k in combinations(n, i):
                a = []
                for l in n:
                    if l not in k:
                        a.append(l)
                for l in combinations(a, j):
                    b = sum(k)
                    c = sum(l)
                    if b == c:
                        return(False)
                        break
                    elif len(k) > len(l) and b < c:
                        return(False)
                        break
    return(True)

def sums(n):
    for i in range(int((n-21)/7), 0, -1):
        for j in range(int((n-15-i)/6), i, -1):
            for k in range(int((n-10-i-j)/5), j, -1):
                for l in range(int((n-6-i-j-k)/4), k, -1):
                    if i+j+k+l < n/2:
                        break
                    for m in range(int((n-3-i-j-k-l)/3), l, -1):
                        for o in range(int((n-1-i-j-k-l-m)/2), m, -1):
                            if special([i, j, k, l, m, o, n-i-j-k-l-m-o]):
                                return(str(i)+str(j)+str(k)+str(l)+str(m)+str(o)+str(n-i-j-k-l-m-o))
                                break
    return(False)

def driver():
    i = 250
    a = sums(i)
    while a == False:
        i+=1
        a = sums(i)
    print(a)

driver()
