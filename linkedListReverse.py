'''
Linked List Reversal
'''

# Define the Linked List Structure
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

# Define the function
def reverseLinkedList(head):
    if not head: return None
    cur = head
    prev = None
    nxt = head
    while nxt:
        cur = nxt
        nxt = nxt.next
        cur.next = prev
        prev = cur
    head = cur
    return head

# Testing
a = Node(10)
b = Node(9, a)
c = Node(8, b)
d = Node(7, c)
e = Node(6, d)
f = Node(5, e)
g = Node(4, f)
h = Node(3, g)
i = Node(2, h)
head = Node(1,i)

print head
print reverseLinkedList(head)