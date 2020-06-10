from math import floor
def pandigitalmultiples():
    p = 0
    d = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(1, 9877):
        isp = True
        ni = ""
        s = ""
        for k in str(i):
            if k in ni:
                isp = False
                break
            else:
                ni+=k
        if isp:
            for j in range(1, floor(9/len(ni))+1):
                s+=str(i*j)
            if sorted([i for i in s]) == d and int(s)>p:
                p = int(s)
    print(p)

pandigitalmultiples()
