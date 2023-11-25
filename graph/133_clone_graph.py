
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        record = {}
        visited = set()

        def dfs1(ptr: Node):
            if ptr in visited: return
            record[ptr.val] = Node(val=ptr.val)
            visited.add(ptr)
            for val in ptr.neighbors:
                dfs1(val)
        dfs1(node)
        visited.clear()

        def dfs2(ptr: Node):
            if not ptr or ptr in visited: return
            for neighbor in ptr.neighbors:
                record[ptr.val].neighbors.append(record[neighbor.val])
                visited.add(ptr)
                dfs2(neighbor)
        dfs2(node)
        return record[node.val]


ptr = Solution()
ptr.cloneGraph(None)

