'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, 
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.

https://leetcode.com/problems/valid-parentheses/
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1: return False
        
        queue = []
        lex = {'}':'{', ')':'(', ']':'['}
        
        for char in s:
            if char == '{' or char == '(' or char == '[':
                queue.append(char)
                completed = False
            else:
                if len(queue) == 0:
                    return False
                elif queue.pop() == lex[char]:
                    if len(queue) == 0: completed = True
                else: return False
                
        if completed: return True
        else: return False
                