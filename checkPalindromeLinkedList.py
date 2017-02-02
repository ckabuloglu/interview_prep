'''
Cracking the Coding Interview
Question 2-5
p.95
(For a *singly linked* list)
'''

# Define the Linked List Node
class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        cur = self
        st = []
        while cur:
            if cur.next:
                st.append(str(cur.data))
                st.append('->')
            else:
                st.append(str(cur.data))
            cur = cur.next
        return ''.join(st)

# Algorithm
def isPalindrome(head):
    fast = head
    slow = head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast: slow = slow.next

    while stack:
        if stack.pop() == slow.data: slow = slow.next
        else: return False
        
    return True

# Testing
l1 = [0,1,2,3,3,2,1,0]
l2 = [0,1,2,3,2,1,0]
l3 = [0,1,2,3,2,1,1]
l4 = [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]

llist = Node(l4[0])
head = llist

for i in l4[1:]:
    llist.next = Node(i)
    llist = llist.next

print head
print isPalindrome(head)  