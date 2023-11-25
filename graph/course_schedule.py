from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visited = set()

        def dfs(course):
            if course in visited: return False
            if not pre_map[course]: return True
            visited.add(course)
            for p in pre_map[course]:
                if not dfs(p): return False
            visited.remove(course)
            pre_map[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True

obj = Solution()
print(obj.canFinish(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
))

