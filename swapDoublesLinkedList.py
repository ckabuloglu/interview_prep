'''
Given a linked list, swap every pair of elements

Given: a -> b -> c -> d
Output: b -> a -> d -> c

Microsoft, 1st round, asked to me
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

# Recursively
def swapRec(head):
    if not head: return None
    elif not head.next: return head

    temp = head.next.next
    head.next.next = head
    head = head.next
    head.next.next = swapRec(temp)
    return head

f = Node('e')
g = Node('d', f)
h = Node('c', g)
i = Node('b', h)
head = Node('a',i)

print head
print swapRec(head)