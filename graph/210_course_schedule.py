from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = [[] for _ in range(numCourses)]
        visited = set()
        order = []
        for course, pre in prerequisites:
            course_map[course].append(pre)

        def dfs(c: int):
            if c in visited: return False
            if not course_map[c]:
                if c not in order: order.append(c)
                return True
            res = True
            visited.add(c)
            for pre in course_map[c]:
                res = res and dfs(pre)
                if not res: return False
            visited.remove(c)
            course_map[c] = []
            order.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c): return []
        return order


