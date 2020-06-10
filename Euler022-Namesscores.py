f = open("/mnt/chromeos/MyFiles/Downloads/Euler problems/p022_names.txt", "r")
g = f.read().split("\",\"")
f.close()
alphabet = {
"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26
}
g[0]="MARY"
g[-1]="ALONSO"
s = 0
t = 0
for i, j in enumerate(g):
    for k in range(i+1, len(g)):
        if g[i] > g[k]:
            a = g[k]
            g[k] = g[i]
            g[i] = a
d = 1
for i in g:
    for j in i:
        s += alphabet[j]
    t += s*d
    s=0
    d+=1
print(t)
