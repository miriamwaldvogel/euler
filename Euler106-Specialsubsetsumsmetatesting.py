def choose(a, b):
    c = 1
    for i in range(b+1, a+1):
        c*=i
    for i in range(2, a-b+1):
        c/=i
    return(int(c))

def meta(n):
    t = 0
    for i in range(2, int(n/2)+1):
        t+=(0.5*choose(n, i)*choose(n-i, i))-(choose(2*i, i)/(i+1))*choose(n, 2*i)
    print(int(t))

meta(12)
