'''
Get Factors of a given number
https://leetcode.com/problems/factor-combinations/?tab=Description
'''

def getFactors(n):
    results = []
    helper(results, [], n, 2)
    results.pop()
    return results

def helper(results, current, n, start):
    if n == 1:
        results.append(list(current))

    for i in range(start, n+1):
        if n % i == 0:
            current.append(i)
            helper(results, current, n / i, i)
            current.pop()
    
print getFactors(18)

