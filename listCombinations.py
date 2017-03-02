'''
Given a list of lists, return a list of all combinations that contains 1 element from each of the given lists
'''

from itertools import product

def allCombinations(arr):
    newArr = []
    helper(arr, newArr, [], 0)
    return newArr

def helper(arr, newArr, item, k):
    if k == len(arr) - 1: 
        for each in arr[k]: newArr.append(item + [each])
    else: 
        for each in arr[k]: helper(arr, newArr, item + [each], k+1)

a = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]
print allCombinations(a)
