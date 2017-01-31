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

# Algorithm (will be completed)
def checkPalindrome():
    return null