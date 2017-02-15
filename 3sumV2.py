'''
3 Sum
Given an array (list) of numbers, and a sum, return 3 elements that have the same given sum.
This provides a better solution that is given in the previous 3sum.py file. Solves the question in O(n^2)
'''

def threeSum(arr, num):
    arr.sort()
    for n in range(len(arr)):
        if arr[n] > (num / 3): return None
        start = n + 1
        end = len(arr) - 1
        target = num - arr[n]
        while not start == end:
            newNum = arr[start] + arr[end] 
            if newNum == target: return (arr[n], arr[start], arr[end])
            elif newNum < target: start += 1
            else: end -= 1
    return None

print threeSum([5,4,3,2,1,0], 6)
