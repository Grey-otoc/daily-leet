class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    res = 0
        
    def dfs(node: TreeNode):
        if node == None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        nonlocal res
        res = max(res, left + right)
        return 1 + max(left, right)
        
    dfs(root)
    return res
    
if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4)))
    print(diameterOfBinaryTree(root))
