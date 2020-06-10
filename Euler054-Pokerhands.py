from re import split
#9=TJQKA same suit, 8=5 consec same suit, 7=4 of a kind, 6=3 of a kind and pair, 5=all same suit, 4=all consec, 3=3 of a kind, 2=2 pairs, 1=1 pair, 0=highest value
#11=J, 12=Q, 13=K, 14=A
f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p054_poker.txt', 'r')
g = split(' |\n', f.read())
f.close()
r = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
h = []
for i in range(1000):
    a = []
    for j in range(2):
        b = []
        for k in range(5):
            b.append(r[g[(10*i)+(5*j)+k][:-1]]+g[(10*i)+(5*j)+k][-1])
        a.append(b)
    h.append(a)

def samesuit(n):
    return(all(i[-1] == n[0][-1] for i in n))

def listmatch(a, b):
    l = len(a)
    return(any(a==b[i:i+l] for i in range(len(b)-l+1)))

def consec(n):
    a = sorted(int(i[:-1]) for i in n)
    if a == [10, 11, 12, 13, 14]:
        return([9])
    elif any(a==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13][i:i+5] for i in range(9)):
        if samesuit(n):
            return([8])
        else:
            return([4])
    return(False)

def repeat(n):
    d = [0]*15
    for i in n:
        a = int(i[:-1])
        d[a] += 1
    if 4 in d:
        return([7, d.index(4)])
    elif 3 in d:
        a = d.index(3)
        if 2 in d:
            return([6, a])
        else:
            return([3, a])
    p = 0
    a = []
    for i, j in enumerate(d):
        if j == 2:
            p += 1
            a.append(i)
    if p > 0:
        return([p, max(a)])
    else:
        return(False)

def poker(n):
    c = consec(n)
    if c != False:
        return(c)
    else:
        r = repeat(n)
        if r != False:
            return(r)
        else:
            if samesuit(n):
                return([5])
            else:
                return([0, max([int(i[:-1]) for i in n])])

def compare(a, b):
    p1 = poker(a)
    p2 = poker(b)
    c = p1[0]
    d = p2[0]
    if c > d:
        return(True)
    elif d > c:
        return(False)
    else:
        e = p1[1]
        f = p2[1]
        if e > f:
            return(True)
        elif f > e:
            return(False)
        else:
            g = sorted([int(i[:-1]) for i in a])
            h = sorted([int(i[:-1]) for i in b])
            g.remove(e)
            h.remove(f)
            i = 3
            while g[i] == h[i]:
                i -= 1
            if g[i] > h[i]:
                return(True)
            else:
                return(False)
t = 0
for i in h:
    if compare(i[0], i[1]):
        t += 1
print(t)
