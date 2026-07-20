class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    def isSameTree(root, sub):
        if root == None and sub == None:
            return True

        if root and sub and root.val == sub.val:
            return (
                isSameTree(root.left, sub.left) 
                and isSameTree(root.right, sub.right)
            )
        
        return False
    
    if not subRoot:
        return True
    if not root:
        return False
    
    if isSameTree(root, subRoot):
        return True
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    subRoot = TreeNode(2, TreeNode(4), TreeNode(5))
    
    print(isSubtree(root, subRoot))
