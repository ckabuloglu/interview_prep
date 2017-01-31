'''
Cracking the Coding Interview
Question 2-3
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

def deleteMiddleNode(node):
    if node and node.next:
        node.data = node.next.data
        node.next = node.next.next
        return True
    else: return False

d = Node(4)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)
head = Node(0, a)

print head
deleteMiddleNode(d)
print head