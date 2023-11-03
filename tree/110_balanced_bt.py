class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        is_balance = True
        def balance_helper(root:TreeNode):
            if not root:
                return 0
            left = balance_helper(root.left)
            right = balance_helper(root.right)
            if abs(left - right) > 1:
                nonlocal is_balance
                is_balance = False
            return max(left,right) + 1
        balance_helper(root)
        return is_balance
        
        
        
