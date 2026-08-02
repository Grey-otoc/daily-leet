class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or not p or not q:
        return None
    if (max(p.val, q.val) < root.val):
        return lowestCommonAncestor(root.left, p, q)
    elif (min(p.val, q.val) > root.val):
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root
    
if __name__ == "__main__":
    p = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    q = TreeNode(8, TreeNode(7), TreeNode(9))
    root = TreeNode(5, p, q)
    res = lowestCommonAncestor(root, p, q)
    print(res.val)
