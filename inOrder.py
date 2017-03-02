'''
Return the in Order list for the given BST tree
'''

# Define the Tree structure
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Define the add method to add nodes to the tree
def add(root, val):
    if not root: return BSTNode(val)
    elif root.val < val: root.right = add(root.right, val)
    else: root.left = add(root.left, val)
    return root

# Define the functions that return a inOrder List for the given BST
def inOrder(root):
    arr = []
    helper(root, arr)
    return arr

def helper(root, arr):
    if not root: return
    helper(root.left, arr)
    arr.append(root.val)
    helper(root.right, arr)

# Define the tree and test
root = BSTNode(10)
add(root, 5)
add(root, 15)
add(root, 13)
add(root, 1)
add(root, 2)
add(root, 21)

print inOrder(root)


