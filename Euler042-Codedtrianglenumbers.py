f = open("/mnt/chromeos/MyFiles/Downloads/Euler problems/p042_words.txt", "r")
g = f.read().split("\",\"")
f.close()
alphabet = {
  "A":1,"B":2,"C":3,"D":4,"E":5, "F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,
  "Z":26
}
g[0] = "A"
g[-1] = "YOUTH"
tn = []
c = 0
t = 0
for i in range(1, 28):
    c += i
    tn.append(c)
for j in g:
    s = 0
    for k in j:
        s+= alphabet[k]
    if s in tn:
        t+=1
print(t)
