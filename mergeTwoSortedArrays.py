'''
Merge two sorted arrays
'''

def mergeTwo(nums1, m, nums2, n):
    if n == 0: nums1 = nums1
    elif m == 0:
        i = 0
        for num in nums2:
            nums1[i] = num
    else:
        i = 0
        j = 0

        while i < m + n and j < n:
            if i == len(nums1):
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
            elif nums2[j] < nums1[i]: 
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
            else:
                i += 1

a = [3, 5, 8, 11, 14]
b = [2, 4, 6, 7, 9, 10, 12, 15, 18, 32]
c = [0]
d = [1]

mergeTwo(a, len(a), d, len(d))
print a