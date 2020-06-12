def productsum(p, s, c, b):
    k = p - s + c
    if k < a:
        if p < n[k]: n[k] = p
        for i in range(b, a//p*2 + 1):
            productsum(p*i, s+i, c+1, i)

a = 12001
n = [2*a] * a
productsum(1, 1, 1, 2)

print(sum(set(n[2:])))
