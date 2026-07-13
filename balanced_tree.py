class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode) -> bool:
    res = True

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        nonlocal res
        
        if abs(left - right) > 1:
            res = False
        return 1 + max(left, right)

    dfs(root)
    return res

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    print(isBalanced(root))
