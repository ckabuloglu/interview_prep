'''
Binary Tree - Least Common Ancestor
UNCOMPLETE
'''

# Define Tree Node data structre
class TreeNode():
    def __init__(self,data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def commonAncestor(root, p, q):
    if not root: return False

    pFound = False
    qFound = False
    if root == p: pFound = True
    elif root == q: qFound = True
    
    right = commonAncestor(root.right, p, q)
    left = commonAncestor(root.left, p, q)