class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        largest = root.val
        return self.dfs(root, largest)
        
    def dfs(self, root: TreeNode, largest:int):
        if root == None:
            return 0
        count = 0
        if root.val >= largest:
            count += 1
        largest = max(largest, root.val)
        
        count += self.dfs(root.left, largest)
        count += self.dfs(root.right, largest)
        return count
        