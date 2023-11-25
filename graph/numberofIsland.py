from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, column = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(x: int, y: int):
            if x < 0 or y < 0 or x >= row or y >= column or grid[x][y] == "0" or tuple([x, y]) in visited:
                return
            visited.add(tuple([x, y]))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return

        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1" and tuple([i, j]) not in visited:
                    res += 1
                    dfs(i, j)

        return res


obj = Solution()
z= obj.numIslands([["1","1","0","0","0"],
                   ["1","1","0","0","0"],
                   ["0","0","1","0","0"],
                   ["0","0","0","1","1"]])


print(z)


# [1,2,3,4,5,-1,2]   target = 2
# visit = set()
# for vals in lst:
#     if (target - vals) in visit:
#         return True
#     if vals not in visit:
#         visit.add(vals)
# return False
