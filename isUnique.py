'''
Cracking the coding interview
Question 1-1
p. 90
'''

from collections import defaultdict

def isUnique(string):
    d = defaultdict(int)
    for c in string:
        if d[c] >= 1: return False
        else: d[c] += 1

    return True

print isUnique('Merhab')
print isUnique('Merhaba')
print isUnique("HaciBerk")
print isUnique('123')
print isUnique('aaaaaaaa')
print isUnique('Aa')