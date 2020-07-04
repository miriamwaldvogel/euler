def reversible(n):
    return(all(int(i)%2 == 1 for i in str(n)))

def rbelow(n):
    t = 0
    for i in range(12, n+1):
        s = int(str(i)[::-1])
        if i < s:
            if reversible(i+s):
                t += 2
    print(t)

rbelow(999999999)
