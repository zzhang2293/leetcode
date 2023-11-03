class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        is_same = self.same(root, subRoot)
        if is_same:
            return is_same
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    
    def same(self, x:TreeNode, y:TreeNode):
        if not x and not y:
            return True
        elif not x or not y or x.val != y.val:
            return False
        
        return self.same(x.left, y.left) and self.same(x.right, y.right)