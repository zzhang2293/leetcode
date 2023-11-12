class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        rows, cols = len(board), len(board[0])
        path, res = set(), False
        def dfs(x:int, y:int, i:int):
            if i == len(words):
                return True
            
            if (x < 0 or y < 0 or x >= rows or y >= cols or words[i] != board[x][y] or (x, y) in path): return False
            
            
            path.add((x, y))
            res = dfs(x + 1, y, i + 1) or dfs(x-1, y, i + 1) or dfs(x, y + 1, i + 1) or dfs(x, y - 1, i + 1)       
            path.remove((x, y))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False