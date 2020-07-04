from math import sqrt

def square(n):
    return(sqrt(n)==int(sqrt(n)))

def collection(n):
    s = [[] for i in range(n+1)]
    for i in range(2, int(sqrt(n))+1):
        a = i**2
        for j in range(1, int(a/2)):
            b = a-j
            if square(b-j):
                s[j].append(b)
                s[b].append(j)
                c = len(s[j])
                d = len(s[b])
                if c > d:
                    e = s[j]
                    f = s[b]
                else:
                    e = s[b]
                    f = s[j]
                for k in f:
                    if k in e:
                        return(k+b+j, e, f, k, b, j, c>d)

print(collection(1000000))
