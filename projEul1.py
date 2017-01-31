import sys

def multiples(num):
    num -= 1
    total = 0
    n = num / 3
    total += 3 * n * (n + 1) / 2
    n = num / 5
    total += 5 * n * (n + 1) / 2
    n = num / 15
    total -= 15 * n * (n + 1) / 2
    
    return total

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print multiples(n)