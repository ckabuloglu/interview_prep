'''
Crakcing the coding interview
4.4
'''
from minimalTree import makeTree

# Define Tree Node data structre
class TreeNode():
    def __init__(self,data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Define the functions
def isBalanced(root):
    if not root: return True
    balance = getHeight(root.left) - getHeight(root.right)
    if abs(balance) > 1: return False
    else: return isBalanced(root.left) and isBalanced(root.right)
        

def getHeight(root):
    if not root: return -1
    else: return max([getHeight(root.left), getHeight(root.right)]) + 1

# Testing
arr = range(10)
root = makeTree(arr)
t = TreeNode(100, root, None)
print isBalanced(t)