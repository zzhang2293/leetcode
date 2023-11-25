from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])

        def is_valid(x: int, y: int) -> bool:
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] != 1: return False
            else: return True

        lst = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2: lst.append((i, j))
        res = 0
        while lst:
            ready = set()
            for i, j in lst:
                if is_valid(i + 1, j) and (i + 1, j) not in lst:
                    ready.add((i + 1, j))
                if is_valid(i - 1, j) and (i - 1, j) not in lst:
                    ready.add((i - 1, j))
                if is_valid(i, j + 1) and (i, j + 1) not in lst:
                    ready.add((i, j + 1))
                if is_valid(i, j - 1) and (i, j - 1) not in lst:
                    ready.add((i, j - 1))
                grid[i][j] = 2
            lst.clear()
            for i, j in ready:
                lst.append((i, j))
            res += 1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1: return -1
        return max(res - 1, 0)


obj = Solution()
x = obj.orangesRotting([[2,2],[1,1],[0,0],[2,0]])
print(x)