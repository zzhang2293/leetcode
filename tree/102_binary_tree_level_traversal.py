class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        order = []
        if root:
            order.append(root)
        res = []
        while order:
            level = []
            for index, val in enumerate(order):
                level.append(val)
            order.clear()
            tmp = []
            for val in level:
                tmp.append(val.val)
                if val.left:
                    order.append(val.left)
                if val.right:
                    order.append(val.right)
            res.append(tmp)
        return res   
    
    

        