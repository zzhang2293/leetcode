from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col, cache, visited = len(matrix), len(matrix[0]), {}, set()

        def dfs(x: int, y: int, pre):
            if x < 0 or y < 0 or x >= row or y >= col: return 0
            if pre >= matrix[x][y] or (x, y) in visited: return 0
            if (x, y) in cache: return cache[(x, y)]
            visited.add((x, y))
            best = 0
            best = max(best, dfs(x + 1, y, matrix[x][y]))
            best = max(best, dfs(x - 1, y, matrix[x][y]))
            best = max(best, dfs(x, y + 1, matrix[x][y]))
            best = max(best, dfs(x, y - 1, matrix[x][y]))
            cache[(x, y)] = best + 1
            visited.remove((x, y))
            return best + 1
        b = 0
        for i in range(row):
            for j in range(col):
                b = max(b, dfs(i, j, float("-infinity")))
        return b


print(Solution().longestIncreasingPath([[9, 9, 4],
                                        [6, 6, 8],
                                        [2, 1, 1]]))


