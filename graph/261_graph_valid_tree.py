from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [x for x in range(n)]
        rank = [1] * n

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return False
            else:
                if rank[p1] > rank[p2]:
                    rank[p1] += rank[p2]
                    parent[p2] = p1
                else:
                    rank[p2] += rank[p1]
                    parent[p1] = p2
            return True

        for n1, n2 in edges:
            if not union(n1, n2): return False
        p_set = set()
        for p in parent:
            p_set.add(find(p))
        if len(p_set) != 1: return False
        return True


print(Solution().validTree(8, [[0, 1], [2, 3], [4, 5], [6, 7], [1, 2], [5, 6], [3, 4]]))
