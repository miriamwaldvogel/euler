def palindrome(n):
    return(str(n) == str(n)[::-1])

def lychrel():
    l = 0
    for i in range(10000):
        p = i+int(str(i)[::-1])
        s = 1
        while not palindrome(p):
            p += int(str(p)[::-1])
            s += 1
            if s > 49:
                l += 1
                break
    print(l)

lychrel()
