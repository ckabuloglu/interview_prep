'''
Cracking the Coding interview
2.7

Find and return the intersection point of two given linked lists if it exists
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

def findIntersection(l1, l2):
    # Go though the first Linked List
    cur = l1
    len1 = 0
    while cur:
        len1 += 1
        if cur.next == None: tail1 = cur
        cur = cur.next

    cur = l2
    len2 = 0
    while cur:
        len2 += 1
        if cur.next == None: tail2 = cur
        cur = cur.next
    
    if tail1 is not tail2: return None

    if len2 > len1: 
        head1 = l2
        head2 = l1
    else:
        head1 = l1
        head2 = l2

    for _ in range(0, abs(len1 - len2)):
        head1 = head1.next
    
    while head1 is not head2:
        head1 = head1.next
        head2 = head2.next

    return head1.data

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
head2 = Node(99, f)
z = Node(100)
head3 = Node(101, z)

print head
print head2
print head3
print findIntersection(head, head2)
print findIntersection(head, head3)