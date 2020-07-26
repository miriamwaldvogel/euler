def batch(n, p):
    if n == 0:
        return([p[0]-1, p[1]+1, p[2]+1, p[3]+1, p[4]+1])
    elif n == 1:
        return([p[0], p[1]-1, p[2]+1, p[3]+1, p[4]+1])
    elif n == 2:
        return([p[0], p[1], p[2]-1, p[3]+1, p[4]+1])
    elif n == 3:
        return([p[0], p[1], p[2], p[3]-1, p[4]+1])
    else:
        return([p[0], p[1], p[2], p[3], p[4]-1])

s = {}
def paper(p, b):
    if b >= 16:
        return(0)
    c = tuple(p)
    if c not in s:
        o = 0
        t = sum(p)
        if t == 1:
            o = 1
        for i, j in enumerate(p):
            if j != 0:
                o += paper(batch(i, p), b+1)*j/t
        s[c] = o
    return(s[c])

print(round(paper([1, 0, 0, 0, 0], 0)-2, 6))
