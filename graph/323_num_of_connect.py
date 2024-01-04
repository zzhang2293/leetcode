from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n)]
        rank = [1] * n

        def find(x):
            par = parent[x]
            while par != parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]
            return par

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return False
            else:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                elif rank[p1] <= rank[p2]:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
                return True
        for n1, n2 in edges:
            if union(n1, n2): n -= 1

        return n


obj = Solution()
print(obj.countComponents(4, [[0,1],[2,3],[1,2]]))
