'''
Cracking the Coding Interview
Question 2-2
p.94
(For a *singly linked* list)
'''

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

def kToLast(head, k):
    if not head: return None
    elif not head.next and k == 1: return head.data

    cur = head
    target = head
    while cur:
        if k == 1 and not cur.next:
            return target.data
        elif k == 1:
            target = target.next
        else:
            k -= 1
        cur = cur.next
    return None

d = Node(4)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)
head = Node(0, a)

head2 = Node(5)

print kToLast(head, 1)
print kToLast(head2, 2)