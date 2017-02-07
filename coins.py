'''
Cracking the Coding interview
8.11
Coin Sum
'''
import timeit
from collections import defaultdict

# Define the function
def makeChange(n, index, coins, memo):
    if n < 0 or index >= len(coins): return 0
    elif n == 0: return 1
    elif memo[(n, index)] > 0: return memo[(n, index)]
    else:
        n1 = makeChange(n - coins[index], index, coins, memo)
        n2 = makeChange(n, index + 1, coins, memo)
        memo[(n, index)] = n1 + n2
        return n1 + n2

# Second way
def makeChange2(n ,index, coins, memo):
    if memo[(n, index)] > 0: return memo[(n, index)]

    if index >= len(coins) - 1: return 1
    coin = coins[index]
    ways = 0
    for i in range(0,n+1,coin):
        rem = n - i
        ways += makeChange2(rem, index + 1, coins, memo)
    memo[(n, index)] = ways
    return ways

# Testing
memo = defaultdict(int)
coins = [200, 100, 50, 20, 10, 5, 2, 1]

start = timeit.default_timer()
print makeChange(10000, 0, coins, memo)
stop = timeit.default_timer()
print stop - start

start = timeit.default_timer()
print makeChange2(10000, 0, coins, memo)
stop = timeit.default_timer()
print stop - start