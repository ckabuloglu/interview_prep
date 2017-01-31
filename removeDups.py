'''
Cracking the Coding Interview
Question 2-1
p.94
(For a *singly linked* list)
'''
from collections import defaultdict

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

def removeDups(head):
    current = head
    if not head: return head
    d = defaultdict(int)
    d[current.data] += 1

    while current.next:
        if d[current.next.data] > 0:
            current.next = current.next.next
        else: 
            d[current.next.data] += 1
            current = current.next
        
    return head

d = Node(1)
a = Node(2, d)
b = Node(2, a)
c = Node(0, b)
head = Node(1, c)

print head
removeDups(head)
print head

