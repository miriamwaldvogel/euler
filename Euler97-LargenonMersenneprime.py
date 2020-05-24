def mersenne(n):
    a = 1863385088
    for i in range(n-16):
        a*=2
        a = int(str(a)[-10:])
    print(a+1)

mersenne(7830457)
