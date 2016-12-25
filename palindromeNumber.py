'''
Determine whether an integer is a palindrome. Do this without extra space.

https://leetcode.com/problems/palindrome-number/
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0: return False
        elif x < 10: return True

        newStr = str(x)
        
        i = 0
        while i < math.floor(len(newStr)/2.0):
            if newStr[i] == newStr[len(newStr) - 1 - i]: i += 1
            else: return False
            
        return True