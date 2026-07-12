class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    if root == None:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))

if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5, TreeNode(8))))
    print(maxDepth(tree))
