# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import itertools

def isConnected(a, b, d):
    visited = [a]
    toGo = list(d[a])
    answer = False
    while toGo:
        now = toGo.pop()
        visited.append(now)
        if now == b:
            answer = True
            break
        for node in d[now]:
            if (node not in visited) and (node not in toGo): toGo.append(node)
    return answer
    

n,t = map(int,raw_input().split())

d = defaultdict(list)
for i in xrange(t):
    a,b = map(int,raw_input().split())
    d[a].append(b) 
    d[b].append(a)

print sum([1 for comb in itertools.combinations(range(n),2) if not isConnected(comb[0], comb[1], d)])