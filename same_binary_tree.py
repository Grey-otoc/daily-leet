class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p == None and q == None:
        return True

    if p and q and p.val == q.val:
        return (
            isSameTree(p.left, q.left) 
            and isSameTree(p.right, q.right)
        )
    else:
        return False
    
if __name__ == "__main__":
    p = TreeNode(1, TreeNode(3), TreeNode(2))
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    print(isSameTree(p, q))
