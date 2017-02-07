'''
Check if a binary tree is a BST
'''
from minimalTree import makeTree

# Define Tree Node data structre
class TreeNode():
    def __init__(self,data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Define the funtion
def checkBST(root):
    if not root: return True
    elif not root.left and not root.right: return True
    elif not root.left and root.right.data < root.data: return False
    elif not root.right and root.left.data > root.data: return False
    else: return checkBST(root.left) and checkBST(root.right)

arr = range(10)
root = makeTree(arr)
t = TreeNode(100, None, root)
print checkBST(t)