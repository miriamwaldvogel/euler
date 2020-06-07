from itertools import combinations
from math import sqrt
f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p098_words.txt', 'r')
g = f.read().split('","')
f.close()
words = [[] for i in range(15)]
words[1].append('A')
words[5].append('YOUTH')
for i in g:
    words[len(i)].append(i)
del words[0]
def anagram(a, b):
    if sorted([i for i in a]) == sorted([i for i in b]):
        return(True)
    else:
        return(False)
for i in range(len(words)-1, -1, -1):
    for j, k in combinations(words[i], 2):
        if anagram(j, k):
            for l in range(int(sqrt(10**(i)))+1, int(sqrt(10**(i+1)))):
                s = {}
                b = True
                for m, n in enumerate(str(l**2)):
                    if n in s.values() and j[m] not in s:
                        b = False
                        break
                    else:
                        s[j[m]] = n
                if b:
                    a = ''
                    for m in k:
                        a+=s[m]
                    if a[0] != '0' and int(sqrt(int(a))) == sqrt(int(a)) and anagram(str(l**2), a):
                        print(max(l**2, int(a)))
                        break
