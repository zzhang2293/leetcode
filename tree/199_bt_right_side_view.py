class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> int:
        res = []
        cur = root
        temp = []
        if cur:
            temp.append(cur)
        while temp:
            lst = []
            for index, val in enumerate(temp):
                lst.append(val)
            if lst:
                res.append(lst[0].val)
            temp.clear()
            for val in lst:
                if val.right:
                    temp.append(val.right)
                if val.left:
                    temp.append(val.left)
        return res