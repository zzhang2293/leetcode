from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, pos_diag, neg_diag = set(), set(), set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                cpy = ["".join(row) for row in board]
                res.append(cpy)
                return
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = 'Q'
                backtrack(r + 1)
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return res
