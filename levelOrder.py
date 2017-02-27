'''
Level Order Traversal
Given a binary tree, print the nodes in order of levels (left to right for same level)
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

# Define the function that print the level order tree Traversal
def levelOrder(root):
    queue = [root]
    levels = []
    while queue:
        current = queue.pop(0)
        if current:
            levels.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else: levels.append(None)
    return levels


# Define the trees and test cases
a = BSTNode(4)
add(a, 3)
add(a, 1)

print levelOrder(a)