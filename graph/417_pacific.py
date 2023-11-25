from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col, res, visited , pacific, atlantic = len(heights), len(heights[0]), [], set(), set(), set()

        def dfs(x: int, y: int, pre_x: int, pre_y: int):
            if x < 0 or y < 0 or x >= row or y >= col or tuple([x, y]) in visited: return
            if len(visited) != 0 and heights[x][y] < heights[pre_x][pre_y]: return
            visited.add(tuple([x, y]))
            dfs(x + 1, y, x, y)
            dfs(x, y + 1, x, y)
            dfs(x - 1, y, x, y)
            dfs(x, y - 1, x, y)
            return
        res = []
        for i in range(col):
            dfs(0, i, -1, -1)
            for val in visited:
                if val not in pacific: pacific.add(val)
            visited.clear()
        for i in range(row):
            dfs(i, 0, -1, -1)
            for val in visited:
                if val not in pacific: pacific.add(val)
            visited.clear()
        for i in range(row):
            dfs(i, col - 1, -1, -1)
            for val in visited:
                if val not in atlantic: atlantic.add(val)
            visited.clear()
        for i in range(col):
            dfs(row - 1, i, -1, -1)
            for val in visited:
                if val not in atlantic: atlantic.add(val)
            visited.clear()
        for val in pacific:
            if val in atlantic:
                res.append(list(val))

        return res


