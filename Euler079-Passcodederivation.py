from itertools import permutations
f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p079_keylog.txt', 'r')
g = f.readlines()
f.close()
chars = ['7', '3', '1', '9', '6', '8', '0', '2']
s = True
for i in permutations(chars, len(chars)):
    s = True
    for j in g:
        j = j[:3]
        a = i.index(j[0])
        b = i.index(j[1])
        c = i.index(j[2])
        if a > b or a > c or b > c:
            s = False
            break
    if s:
        t = ''
        for k in i:
            t+=k
        print(t)
        break
