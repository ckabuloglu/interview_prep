'''
Cracking the coding interview
8.2
p. 135

Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
The robot can only move in two directions, right and down, but certain cells are "off limits" such 
that the robot cannot step on them. Design an algorithm to find a path for the robot from the top 
left to the bottom right
'''

# Define the functions
def grid(m, n):
    memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    return robotGrid(m, n, m, n, memo)

def robotGrid(r,c,m,n, memo):
    if r < 1 or c < 1 or r > m or c > n: return 0
    elif r == 1 or c == 1: return 1
    elif memo[r][c] > -1: return memo[r][c]
    else:
        memo[r][c] = robotGrid(r-1, c, m, n, memo) + robotGrid(r, c-1, m, n, memo)
        return memo[r][c]

# Test the functions
print grid(2, 2)
print grid(3, 3)
print grid(20, 20)