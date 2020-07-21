def path(n):
    a = [[1, 2]]
    while True:
        t = []
        for i in a:
            for j in i:
                p = i+[i[-1]+j]
                if p[-1] == n:
                    return(len(p)-1)
                    break
                elif p[-1] < n:
                    t.append(p)
        a = t

def efficient(n):
    t = 1
    for i in range(3, n+1):
        t += path(i)
    print(t)

efficient(200)
