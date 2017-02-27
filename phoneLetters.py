'''
LeetCode - Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/?tab=Description
Given a digit string, return all possible letter combinations that the number could represent.
'''

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    
    d = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],}
    combs = [[]]
            
    for digit in digits:
        temp = []
        for char in d[digit]:
            for comb in combs:
                newComb = list(comb)
                newComb.append(char)
                temp.append(newComb)
        combs = temp
        # if len(combs) < 5: combs.pop(0)
    if len(combs) == 1: return []
    combs = [''.join(comb) for comb in combs]
    return combs