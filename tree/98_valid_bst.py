class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        scope = [float("-infinity"), float("infinity")]
        
        return self.isValidHelper(root, scope)
    def isValidHelper(self, root:TreeNode, scope):
        if not root:
            return True
        if not (scope[0] < root.val < scope[1]):
            return False
        return self.isValidHelper(root.left, [scope[0], root.val]) and self.isValidHelper(root.right, [root.val, scope[1]])
    
root = TreeNode(5, left=TreeNode(val=4), right=TreeNode(val=6, left=TreeNode(val=3), right=TreeNode(val=7)))
obj = Solution()
print(obj.isValidBST(root))