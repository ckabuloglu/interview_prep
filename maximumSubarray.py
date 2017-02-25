'''
Maximum sub-array
Leetcode

Given an array with at least 1 element, return the sum of a sub-array with the maximum sum
'''

def maxSum(nums):
    mx = nums[0]
    until = nums[0]
    
    for i in range(1,len(nums)):
        until = max(until + nums[i] , nums[i])
        mx = max(mx, until)	

    return mx

    
a = [-2,1,-3,4,-1,2,1,-5,4]
b = [5, 5, 4, -15, 5, 5, 5]
c = [-1, -3, -1, -4, 0]
d = [10]
e = [1,2,-1,-2,2,1,-2,1,4,-5,4]
f = [3, 3, 3, 3, 5, -11, 5]

print maxSum(a)
print maxSum(b)
print maxSum(c)
print maxSum(d)
print maxSum(e)
print maxSum(f)
