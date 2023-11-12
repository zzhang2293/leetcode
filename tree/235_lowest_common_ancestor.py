class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == q :
            return p
        if p == root:
            return p
        if q == root:
            return q
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
    
    
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
obj = Solution()
val = obj.lowestCommonAncestor(root, root.left, root.right)
print(val.val)