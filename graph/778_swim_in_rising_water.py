from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap, visited = [[grid[0][0], 0, 0]], set()
        res, row, col = 0, len(grid), len(grid[0])
        while (row - 1, col - 1) not in visited:
            height, x, y = heapq.heappop(heap)
            visited.add((x, y))
            res = max(res, height)
            if x - 1 >= 0 and (x - 1, y) not in visited:
                heapq.heappush(heap, [grid[x - 1][y], x - 1, y])
            if x + 1 < row and (x + 1, y) not in visited:
                heapq.heappush(heap, [grid[x + 1][y], x + 1, y])
            if y - 1 >= 0 and (x, y - 1) not in visited:
                heapq.heappush(heap, [grid[x][y - 1], x, y - 1])
            if y + 1 < col and (x, y + 1) not in visited:
                heapq.heappush(heap, [grid[x][y + 1], x, y + 1])
        return res


print(Solution().swimInWater(
    [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
