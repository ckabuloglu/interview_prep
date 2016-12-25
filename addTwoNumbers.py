'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

https://leetcode.com/problems/add-two-numbers/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        node = None
        while l1 != None or l2 != None or carry == 1:
            digit = 0
            
            if l1 != None:
                digit += l1.val
                l1 = l1.next
                
            if l2 != None:
                digit += l2.val
                l2 = l2.next
            
            digit += carry
            if digit > 9: carry = 1
            else: carry = 0
            
            digit = digit % 10
            
            if node != None: 
                node.next = ListNode(digit)
                node = node.next
            else:
                node = ListNode(digit)
                node1 = node

        return node1
        