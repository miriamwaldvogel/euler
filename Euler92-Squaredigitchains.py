def digitsquare(n):
    s = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    t = 0
    for i in str(n):
        t += s[int(i)]
    return(t)

def digitchains(n):
    e = [0 for i in range(n+1)]
    f = [0 for i in range(n+1)]
    e[89] = 1
    f[1] = 1
    for i in range(1, n):
        a = i
        b = []
        while a != 1 and a != 89:
            b.append(a)
            a = digitsquare(a)
            if e[a] == 1:
                for j in b:
                    e[j] = 1
                break
            elif f[a] == 1:
                for j in b:
                    f[j] = 1
                break
    print(sum(e))

digitchains(10000000)
