class TreeNode:    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = None
        
        def pathHelper(root:TreeNode):
            nonlocal res
            if not root:
                return 0
            left = max(pathHelper(root.left), 0)
            right = max(pathHelper(root.right), 0)
            
            res = left + right + root.val if res == None else max(res, right + root.val + left)
            res = max(res, root.val + max(left, right))
            return root.val + max(left, right)
        
        pathHelper(root)
        
        return res
            
            
        
    
            