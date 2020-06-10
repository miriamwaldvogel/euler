def digitfactorial(n):
    d = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return(sum(d[int(i)] for i in str(n)))

def chains(n):
    l = [1]*3+[0]*(n-2)
    l[145] = 1
    l[169] = 3
    l[871] = 2
    l[872] = 2
    l[1454] = 3
    t = 0
    for i in range(3, n):
        if l[i] == 0:
            a = [i]
            b = digitfactorial(i)
            while b not in a:
                if b > len(l)-1:
                    l += [0]*(b-len(l)+1)
                    #print(b)
                if l[b] != 0:
                    break
                a.append(b)
                b = digitfactorial(b)
                #print(b)
            #print(a)
            for j, k in enumerate(a):
                l[k] = len(a)-j+l[b]
                if l[k] == 60:
                    t += 1
    print(t)

chains(1000000)
