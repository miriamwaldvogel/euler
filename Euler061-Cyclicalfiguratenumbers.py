def cyclical(n):
    return (3,int(n*(n+1)/2)), (4,n*n), (5,int(n*(3*n-1)/2)), (6,n*(2*n-1)), (7,int(n*(5*n-3)/2)), (8,n*(3*n-2))

def cycle(t, n):
    if len(t) == 6 and int(n[0]/100) == n[-1] % 100:
        print(n, sum(n))
    else:
        for i, j in d.get((t[-1], n[-1]), []):
            if i not in t:
                cycle(t+[i], n+[j])

p = []
i = 19

while i < 141:
    for j, k in cyclical(i):
        if 1000 <= k <= 9999 and k % 100 > 9:
            p.append((j, k))
    i+=1

d = {}
for i, j in p:
    for k, l in p:
        if i != k and j % 100 == l // 100:
            d[i, j] = d.get((i, j),[]) + [(k, l)]

for i, j in d:
    cycle([i], [j])
