from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        visited = set()
        largest = 0

        def dfs(x: int, y: int):
            if x < 0 or y < 0 or x >= row or y >= column or grid[x][y] == 0 or tuple([x, y]) in visited:
                return 0
            visited.add(tuple([x, y]))
            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y - 1) + dfs(x, y + 1)

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1 and tuple([i, j]) not in visited:
                    largest = max(dfs(i, j), largest)
        return largest