'''
Crakcing the coding interview
4.2
'''

class TreeNode():
    def __init__(self,data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def makeTree(arr):
    if len(arr) == 1:
        return TreeNode(arr[0])
    elif len(arr) == 2:
        return TreeNode(arr[1], TreeNode(arr[0]), None)
    else:
        ind = len(arr) / 2
        return TreeNode(arr[ind], makeTree(arr[:ind]), makeTree(arr[ind+1:]))

a = range(9)
tree = makeTree(a)
print tree.data
print tree.left.data
print tree.right.data