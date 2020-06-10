from itertools import permutations
f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p059_cipher.txt', 'r')
g = f.read().split(',')
f.close()
frq = {}
for i in g:
    if i not in frq:
        frq[i] = 1
    else:
        frq[i] += 1
v = sorted(frq.values())
t = 0
for i in permutations(range(97, 123), 3):
    k = list(i)
    k.append(112)
    s = ''
    for j, l in enumerate([36,22,80,0,0,4,23,25,19,17,88,4,4,19,21,11,88]):
        a = l^k[j%3]
        pos = True
        if 32<=a<=90 or 97<=a<=122:
            s += chr(l^k[j%3])
        else:
            pos = False
            break
key = (101, 120, 112)
s = ''
for i, j in enumerate(g):
    s += chr(int(j)^key[i%3])
    t += int(j)^key[i%3]

print(s)
print(t)
