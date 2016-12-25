'''
Given a linked list, remove the nth node from the end of list and return its head.

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None: return []
        
        node = head
        index = 0
        
        while node != None:
            if index == n:
                target = head
                if n == 1: targetNext = None
                else: targetNext = target.next.next
                index += 1
            elif index == n + 1:
                target = target.next
                if n == 1: targetNext = None
                else: targetNext = targetNext.next
            else:
                index += 1
                
            node = node.next
            if node == None:
                if n == index:
                    head = head.next
                else:
                    target.next = targetNext
                
        return head