from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        traveled = set()

        def dfs(x: int, y: int, ptr: int):
            if ptr == len(word): return True
            if (x < 0 or x >= row or y < 0 or y >= col or tuple([x, y]) in traveled or
                    board[x][y] != word[ptr]): return False
            traveled.add(tuple([x, y]))
            res = (
                    dfs(x + 1, y, ptr + 1) or
                    dfs(x - 1, y, ptr + 1) or
                    dfs(x, y + 1, ptr + 1) or
                    dfs(x, y - 1, ptr + 1)
            )
            traveled.remove(tuple([x, y]))
            return res

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0): return True
        return False
