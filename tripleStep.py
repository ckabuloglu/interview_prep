'''
Cracking the coding interview
8.1
p. 134
'''

# Define the function
def wrapper(n):
    memo = [-1 for _ in range(n+1)]
    return numSteps(n, memo)

def numSteps(n, memo):
    if n < 0: return 0
    elif n == 0: return 1
    elif memo[n] > -1 : return memo[n]
    else:
        memo[n] = numSteps(n-1, memo) + numSteps(n-2, memo) + numSteps(n-3, memo)
        return memo[n]

# Testing
print wrapper(3)
print wrapper(4)
print wrapper(5)
print wrapper(20)
