from random import randint
def dice(n):
    return((randint(1, n), randint(1, n)))

def nextrailway(n):
    if n > 34:
        return(5)
    else:
        return((((n+5)/10)*10)+5)

def nextutility(n):
    if 11 < n < 28:
        return(28)
    else:
        return(12)
def monopoly(n, d):
    #GO: 0, community chest: 2, 17, 33, chance: 7, 22, 36, railway: 5, 15, 25, 35, utility: 12, 28
    #community chest(2/16): 0, 10
    #chance(10/16): 0, 10, 11, 24, 39, 5, next railway, next railway, next utility, back 3
    #go to jail: 30 jail: 10
    p = 0
    freq = [0 for i in range(40)]
    chance = [0, 10, 11, 24, 39, 5]
    doubles = 0
    s = ''
    for i in range(n):
        r = dice(d)
        p+=sum(r)
        if r[0] == r[1]:
            doubles += 1
        else:
            doubles = 0
        if doubles == 3 or p == 30:
            p = 10
        elif p == 2 or p == 17 or p == 33:
            a = randint(1, 16)
            if a == 1:
                p = 0
            elif a == 2:
                p = 10
        elif p == 7 or p == 22 or p == 36:
            a = randint(1, 16)
            if a < 6:
                p = chance[a]
            elif a == 6 or a == 7:
                p = nextrailway(p)
            elif a == 8:
                p = nextutility(p)
            elif a == 9:
                p -= 3
        if p > 39:
            p -= 39
        freq[p]+=1
    for i in range(3):
        a = max(freq)
        b = freq.index(a)
        if b > 9:
            s += str(b)
        else:
            s+='0'
            s+=str(b)
        freq[b] = 0
    print(s)
monopoly(1000000, 4)
