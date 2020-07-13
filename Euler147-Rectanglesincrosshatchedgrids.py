def straight(a, b):
    return(int((((a**2)+a)*((b**2)+b))/4))

def cross(a, b):
    return(int((b*((2*a-b)*(4*b*b-1)-3))/6))

def rectangles(a, b):
    t = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            t += cross(max([i, j]), min([i, j]))+straight(i, j)
    print(t)

rectangles(47, 43)
