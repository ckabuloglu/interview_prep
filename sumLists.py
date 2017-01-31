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

def sumLists(num1, num2, carry=0):
    if num1: 
        n1 = num1.data
        num1 = num1.next
    else: n1 = 0

    if num2: 
        n2 = num2.data
        num2 = num2.next
    else: n2 = 0

    n3 = n1 + n2 + carry
    if n3 > 9 and (num1 or num2):
        n3 = n3 % 10
        carry = 1
    else: carry = 0

    if not num1 and not num2: return Node(n3)
    else: return Node(n3, sumLists(num1, num2, carry))

a = Node(6)
b = Node(1,a)
num1 = Node(7, b)
print num1

c = Node(2)
d = Node(9, c)
num2 = Node(5,d)
print num2

print sumLists(num1, num2)