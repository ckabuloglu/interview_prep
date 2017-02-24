'''
Leetcode
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Define the Linked List Structure
class Node:
    def __init__(self, data=None, next=None):
        self.val = data
        self.next = next

    def __repr__(self):
        cur = self
        st = []
        while cur:
            if cur.next:
                st.append(str(cur.val))
                st.append('->')
            else:
                st.append(str(cur.val))
            cur = cur.next
        return ''.join(st)

# Iterative
def mergeTwoLists(l1, l2):
    if not l1: return l2
    elif not l2: return l1

    if l2.val >= l1.val: 
        head = l1
        cur1 = l1.next
        cur2 = l2
    else:
        head = l2
        cur1 = l2.next
        cur2 = l1 
    runner = head

    while cur1 or cur2:
        if not cur2: 
            runner.next = cur1
            return head
        elif not cur1:
            runner.next = cur2
            return head
        elif cur1.val <= cur2.val:
            runner.next = cur1
            cur1 = cur1.next
            runner = runner.next
        else: 
            runner.next = cur2
            cur2 = cur2.next
            runner = runner.next
    return head

# Recursive
def mergeTwoListsRec(l1, l2):
        if not l1: return l2
        elif not l2: return l1
        elif l2.val < l1.val: 
            l2.next = mergeTwoListsRec(l1, l2.next)
            return l2
        else:
            l1.next = mergeTwoListsRec(l1.next, l2)
            return l1

d = Node(8)
a = Node(3,d)
b = Node(2,a)
l1 = Node(1,b)

l2 = Node(4)

print mergeTwoLists(l1, l2)
print mergeTwoListsRec(l1, l2)

