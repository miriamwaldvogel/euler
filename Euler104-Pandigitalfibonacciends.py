import time
def pandigital(n):
    if sorted([i for i in n]) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return(True)
    else:
        return(False)

def fib():
    a = 2504730781961
    b = 1548008755920
    d = a
    e = b
    i = 61
    while not pandigital(str(a)[:9]) or not pandigital(str(d)):
        c = a
        a+=b
        b = c
        c = d
        d+=e
        e = c
        d = int(str(d)[-9:])
        e = int(str(e)[-9:])
        if a > 999999999999999:
            a=int(a/10)
            b=int(b/10)
        i+=1
    print(i)

fib()
