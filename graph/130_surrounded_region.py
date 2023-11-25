from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col, visited = len(board), len(board[0]), set()

        def dfs(x, y):
            if (x, y) in visited: return False
            if x == 0 or y == 0 or x == row - 1 or y == col - 1:
                if board[x][y] == "O": return True
                elif board[x][y] == "X": return False
            if board[x][y] == "X": return False
            visited.add((x, y))
            return dfs(x + 1, y) or dfs(x - 1, y) or dfs(x, y + 1) or dfs(x, y - 1)

        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if board[i][j] == 'O' and (i, j) and not dfs(i, j):
                    for val in visited:
                        x, y = val
                        board[x][y] = "X"
                visited.clear()