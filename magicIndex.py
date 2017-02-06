'''
Cracking the coding interview
8.3
p. 135

Magic Index: A magic index in an array A[1. .. n-1] is defined to be an index such that A[i]
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
'''

# Wrapper function
def magic(arr):
    return findMagic(arr, 0, len(arr)-1)

# Define the problem solving function
def findMagic(arr, start, end):
    mid = (end - start) / 2
    mid = start + mid
    if start > end:
        return None
    elif arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        end = mid - 1
    elif arr[mid] < mid:
        start = mid + 1
    return findMagic(arr, start, end)

# Testing
a = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15, 18, 19, 20, 21, 98, 123, 1235]
print magic(a)

