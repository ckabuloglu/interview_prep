'''
2 Sum
Given an array (list) of numbers, and a sum, return 2 elements that have the same given sum.
'''

def twoSum(arr, num):
    start = 0
    end = len(arr) - 1
    arr.sort()

    while start != end:
        newSum = arr[start] + arr[end]
        if newSum == num: return (arr[start], arr[end])
        elif newSum < num: start += 1
        else: end -= 1

    return None

print twoSum([1, 11, 7, 3, 4, 2, 8, 9], 7)
    