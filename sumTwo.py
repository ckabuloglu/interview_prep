'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

https://leetcode.com/problems/two-sum/
'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numDict = {}
    for i in range(0,len(nums)):   
        if nums[i] in numDict.iterkeys() and i != numDict[nums[i]]: return [numDict[nums[i]], i]
        numDict[target - nums[i]] = i

print twoSum([1,2,3], 3)
print twoSum([2,7,11,15], 9)
print twoSum([3,2,4], 6)
print twoSum([0, 2, 2, 3, 4, 0], 0)
print twoSum([-1,-2,-3,-4,-5], -8)