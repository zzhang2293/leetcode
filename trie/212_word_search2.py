class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

        
class Trie:

    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
            
        return cur.end_of_word

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        visit = set()
        trie = Trie()
        row, col = len(board), len(board[0])
        res = set()
        for word in words:
            trie.insert(word)
            
        
        def dfs(x, y, word:str, node:Node):
            if x < 0 or y < 0 or x >= row or y >= col or (x, y) in visit or board[x][y] not in node.children:
                return
            visit.add((x, y))
            word += board[x][y]
            node = node.children[board[x][y]]
            if node.end_of_word:
                res.add(word)

            dfs(x + 1, y, word, node)
            dfs(x - 1, y, word, node)
            dfs(x, y + 1, word, node)
            dfs(x, y - 1, word, node)
            visit.remove((x, y))
            return
        for i in range(row):
            for j in range(col):
                dfs(i, j, "")
        return list(res)
        