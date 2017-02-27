'''
LeetCode - Reverse Words in a String II
https://leetcode.com/problems/reverse-words-in-a-string-ii/?tab=Description

For example,
Given s = "the sky is blue"
return "blue is sky the"
'''

def reverseWords(s):
    s.reverse()
    
    start = 0
    for i in range(len(s)):
        if s[i] == ' ':
            s[start:i] = reversed(s[start:i])
            start = i + 1
        elif i == len(s) - 1: 
            s[start:i+1] = reversed(s[start:i+1])
            return s

print reverseWords(list("the sky is blue"))
print reverseWords(list("abcabcabc"))

            