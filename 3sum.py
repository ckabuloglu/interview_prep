'''
Given an array S of n integers, are there elements a, b, c in 
S such that a + b + c = 0? Find all unique triplets in 
the array which gives the sum of zero.

https://leetcode.com/problems/3sum/
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = {}
        nums.sort()
        numscopy = nums * 1
        for num in nums:
            if num == 0: continue
            elif num not in count.keys(): count[num] = 1
            elif count[num] <= 1: count[num] += 1
            elif count[num] > 1: numscopy.remove(num)
        nums = numscopy

        dict = {}
        if len(nums) < 3: return []
        if minNum > 0 or maxNum < 0: return []
        
        for i in range(0, len(nums)):
            if nums[i] > 0: break
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] > 0: break
                for k in range(j+1, len(nums)):
                    if nums[k] < 0: continue
                    elif abs(nums[i] + nums[j]) < nums[k]: break
                    if nums[i]+nums[j]+nums[k] == 0: 
                        trip = [nums[i], nums[j], nums[k]]
                        triplet = frozenset(trip)
                        dict[triplet] = trip
                        
        return dict.values()