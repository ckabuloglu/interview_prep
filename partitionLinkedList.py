'''
Cracking the Coding Interview
Question 2-4
p.94
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

# Actual algorithm
def partition(head, x):
    gHead = None
    g = None
    lHead = None
    l = None

    while head:
        if head.data >= x:
            if g: 
                g.next = Node(head.data)
                g = g.next
            else: 
                g = Node(head.data)
                gHead = g
        else:
            if l: 
                l.next = Node(head.data)
                l = l.next
            else:
                l = Node(head.data)
                lHead = l
        head = head.next

    if not lHead: lHead = gHead
    else: l.next = gHead

    return lHead

# Testing
a = Node(2)
b = Node(2, a)
c = Node(10, b)
d = Node(5, c)
e = Node(8, d)
f = Node(5, e)
head = Node(3, f)

print head
head = partition(head, 5)
print head


