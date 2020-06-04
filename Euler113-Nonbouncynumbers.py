def choose(a, b):
    c = 1
    for i in range(a-b+1, a+1):
        c*=i
    for i in range(2, b+1):
        c/=i
    return(int(c))

def nonbouncy(n):
    print(choose(n+9, 9)+choose(n+10, 10)-(10*n)-1)

nonbouncy(100)
