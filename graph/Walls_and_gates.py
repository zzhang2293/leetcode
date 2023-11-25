from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def is_valid(a: int, b: int):
            if (a < 0 or b < 0 or a >= row or b >= col or
                    rooms[a][b] == 0 or rooms[a][b] == -1 or
                    (a, b) in visited):
                return False

            return True

        queue, start, visited, child = set(), 0, set(), set()
        row, col = len(rooms), len(rooms[0])
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.add((i, j))
        while queue:
            for val in queue:
                x, y = val
                visited.add((x, y))
                rooms[x][y] = min(rooms[x][y], start)
                if is_valid(x + 1, y): child.add((x + 1, y))
                if is_valid(x - 1, y): child.add((x - 1, y))
                if is_valid(x, y + 1): child.add((x, y + 1))
                if is_valid(x, y - 1): child.add((x, y - 1))
            queue.clear()
            [queue.add(val) for val in child]
            child.clear()
            start += 1

obj = Solution()
res = obj.wallsAndGates([[2147483647,-1,0,2147483647],
                   [2147483647,2147483647,2147483647,-1],
                   [2147483647,-1,2147483647,-1],
                   [0,-1,2147483647,2147483647]])

print(res)
