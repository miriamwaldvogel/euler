from itertools import combinations
f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p105_sets.txt', 'r')
g = f.read().split('\n')
f.close()

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

t = 0
for i in g:
    a = [int(j) for j in i.split(',') if j != '']
    #print(a)
    if special(a):
        t+=sum(a)
        #print(a)
print(t-4)
