class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        res = None
        def track(root:TreeNode):
            nonlocal count
            nonlocal res
            if not root:
                return
            track(root.left)
            if count >= k:
                return res
            count += 1
            if count == k:
                res = root.val
                return res
            
            track(root.right)
            
            if count >= k:
                return res
        track(root)
        return res
    
    def kthSmallest2(self, root:TreeNode, k:int):
        n = 0
        stack = []
        cur = root
        while cur and stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
            
            
            