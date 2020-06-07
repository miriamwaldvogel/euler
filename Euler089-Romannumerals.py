f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p089_roman.txt', 'r')
g = f.read().split('\n')
f.close()
a = ['VIIII', 'LXXXX', 'DCCCC']
b = ['IIII', 'XXXX', 'CCCC']
t = 0
for i in g:
    for j in range(3):
        if a[j] in i:
            t+=3
        elif b[j] in i:
            t+=2
print(t)
