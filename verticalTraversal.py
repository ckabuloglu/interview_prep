from collections import defaultdict

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define the add method to add nodes to the tree
def add(root, value):
    if not root: return BSTNode(value)
    elif root.value < value: root.right = add(root.right, value)
    else: root.left = add(root.left, value)
    return root

def verticalHelper(root, vertical, level):
    if root == None: return
    vertical[level].append(root.value)
    verticalHelper(root.left, vertical, level - 1)
    verticalHelper(root.right, vertical, level + 1)

def verticalTraversal(root):
    level = 0
    result = defaultdict(list)
    verticalHelper(root, result, level)
    verticalList = []

    print result
    for i in sorted(result.keys()):
        verticalList.append(result[i])

    return verticalList

root = BSTNode(3)
add(root, 1)
add(root, 2)
add(root, 20)
add(root, 15)
add(root, 27)

print verticalTraversal(root)