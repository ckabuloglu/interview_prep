'''
Add all numbers between 0's and store them in-place
linked list is 1->2->3->0->5->4->0->3->2->0
=>  6->9->5
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

def addListElements(head):
    ans = head
    acc = 0
    while head:
        if head.next.data == 0:
            if not head.next.next:
                head.next = None
                break
            else:
                head = head.next
        else:
            head.data += head.next.data
            head.next = head.next.next
    return ans
            
a = Node(0)
b = Node(2, a)
c = Node(3, b)
d = Node(0, c)
e = Node(4, d)
f = Node(5, e)
g = Node(0, f)
h = Node(3, g)
i = Node(2, h)
head = Node(1,i)

print head
print addListElements(head)