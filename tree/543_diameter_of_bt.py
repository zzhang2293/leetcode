class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d, h = self.maxDepthHelper(root)
        return d
    def maxDepthHelper(self, root: TreeNode) -> tuple(int, int):
        if not root:
            return 0, 0
        left, right = root.left, root.right
        d_left, height_left = self.maxDepthHelper(left)
        d_right, height_right = self.maxDepthHelper(right)
        height = 1 + max(height_left, height_right)
        diameter = height_left + height_right
        return max(d_left, max(d_right, diameter)), height