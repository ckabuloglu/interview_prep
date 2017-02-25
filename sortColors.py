'''
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color 
red, white, and blue respectively.
'''

# Define the function
def sortColors(arr):
    pointer0 = 0
    pointer2 = len(arr) - 1
    i = 0

    while i <= pointer2:
        if arr[i] == 0:
            swap(arr, i, pointer0)
            pointer0 += 1
        elif arr[i] == 2:
            swap(arr, i, pointer2)
            pointer2 -= 1
        i += 1
    return arr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# Define the test cases
a = [0, 0, 0, 1, 1, 1, 2, 2, 2]
b = [2, 1, 0]
c = [1, 1, 1, 0, 0, 0]
d = [2, 2, 2, 2, 0, 0, 0, 0]

print sortColors(a)
print sortColors(b)
print sortColors(c)
print sortColors(d)




