from itertools import permutations
from itertools import combinations
def primepermutations():
    l = 9999
    isprime = [True] * (l+1)
    p = 2
    while p * p <= l:
        if isprime[p]:
            for i in range(2*p, l+1, p):
                    isprime[i] = False
        p+=1
    for i in range(1000, l+1):
        if isprime[i]:
          pt = []
          for j in permutations(str(i)):
              a = "".join(j)
              if isprime[int(a)] and int(a) > 999:
                  pt.append(int(a))
                  isprime[int(a)] = False
          if len(pt) > 2:
              d = {}
              for l in combinations(pt, 2):
                  m = sorted(l)
                  b = m[1]-m[0]
                  if b in d:
                      d[b][0] += 1
                      d[b].append(m)
                      if d[b][1][1] == d[b][2][0] or d[b][1][0] == d[b][2][1]:
                          print(str(d[b][1][0])+str(d[b][1][1])+str(d[b][2][1]))
                  else:
                      d[b] = [1]
                      d[b].append(m)
primepermutations()
