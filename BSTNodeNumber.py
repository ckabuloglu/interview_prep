'''
Return the number of nodes found in the given Binary Search Tree
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

# Define the function to count the number of nodes
def countNodes(root):
    if not root: return 0
    return countNodes(root.left) + 1 + countNodes(root.right)

# Define the tree and testing
root = BSTNode(10)
add(root, 11)
add(root, 12)
add(root, 13)
add(root, 14)
add(root, 15)
add(root, 16)

print countNodes(root)