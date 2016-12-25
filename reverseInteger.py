'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

https://leetcode.com/problems/reverse-integer/
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = True if x < 0 else False
        numStr = str(abs(x))
        ans = ""
        for letter in numStr:
            ans = letter + ans
        
        if neg:
            ans = '-' + ans
        
        ans = int(ans)
        if ans < (-(2**31) + 1) or ans > 2**31: ans = 0
        return ans