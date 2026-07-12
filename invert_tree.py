class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    if root == None:
        return None

    root.right, root.left = root.left, root.right

    invertTree(root.left)
    invertTree(root.right)

    return root

def printValues(root: TreeNode):
    print(root.val)
    
    if root.left:
        printValues(root.left)
    if root.right:
        printValues(root.right)
    
if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(2), TreeNode(1))
    
    inverted = invertTree(tree)
    printValues(inverted)
