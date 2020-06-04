def bouncy(n):
    a = [i for i in str(n)]
    b = sorted(a)
    if b != a and b[::-1] != a:
        return(True)
    else:
        return(False)

def driver():
    a = 100
    b = 0
    while b != a*0.99:
        for i in range(a+1, a+101):
            if bouncy(i):
                b+=1
        a+=100
        #print(a)
    print(a, b)

driver()
