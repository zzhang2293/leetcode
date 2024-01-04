from typing import Optional


class TrieNode:

    def __init__(self) -> None:
        self.nxt: list[Optional[TrieNode]] = [None] * 26
        self.Pass: int = 0
        self.end: int = 0
        return


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()
        return

    def insert(self, word: str) -> None:
        cur = self.root
        cur.Pass += 1
        for i in range(len(word)):
            c = ord(word[i]) - ord("a")
            if not cur.nxt[c]: cur.nxt[c] = TrieNode()
            cur = cur.nxt[c]
            cur.Pass += 1
        cur.end += 1
        return

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for ind, val in enumerate(word):
            if not cur.nxt[ord(val) - ord("a")]: return 0
            cur = cur.nxt[ord(val) - ord("a")]
        return cur.end

    def countWordStartingWith(self, word: str) -> int:
        cur = self.root
        for ind, val in enumerate(word):
            if not cur.nxt[ord(val) - ord("a")]: return 0
            cur = cur.nxt[ord(val) - ord("a")]
        return cur.Pass

    def erase(self, word: str) -> None:
        if not self.countWordsEqualTo(word): return
        cur = self.root
        cur.Pass -= 1

        for ind, val in enumerate(word):
            path = ord(val) - ord("a")
            cur.nxt[path].Pass -= 1
            if cur.nxt[path].Pass == 0:
                cur.nxt[path] = None
                return
            cur = cur.nxt[path]
        cur.end -= 1
        return


""" better solution """


class Trie2:
    """ number of input """
    MAX_N: int = 100
    """ mapping """
    tree: list[list[int]] = [[0] * 26 for _ in range(MAX_N)]
    """ register end of a value """
    end: list[int] = [0] * MAX_N
    """ number of word that is pass this char """
    path: list[int] = [0] * MAX_N
    """use this to allocate a new row for a new node"""
    alloc: int = 0

    def __init__(self) -> None:
        Trie2.alloc = 1

    def insert(self, word: str) -> None:
        # start at current row (node)
        cur = 1
        Trie2.path[cur] += 1
        for ind, val in enumerate(word):
            path = ord(val) - ord("a")
            if Trie2.tree[cur][path] == 0:
                Trie2.alloc += 1
                Trie2.tree[cur][path] = Trie2.alloc
            Trie2.path[cur] += 1
            cur = Trie2.tree[cur][path]
        Trie2.end[cur] += 1
        return

    def countWordsEqualTo(self, word: str) -> int:
        cur = 1
        for ind, val in enumerate(word):
            path = ord(val) - ord("a")
            if Trie2.tree[cur][path] == 0: return 0
            cur = Trie2.tree[cur][path]
        return Trie2.end[cur]

    def countWordsStartingWith(self, word: str) -> int:
        cur = 1
        for ind, val in enumerate(word):
            path = ord(val) - ord("a")
            if Trie2.tree[cur][path] == 0: return 0
            cur = Trie2.tree[cur][path]
        return Trie2.path[cur]

    def erase(self, word: str) -> None:
        if self.countWordsEqualTo(word) == 0: return
        cur = 1
        for ind, val in enumerate(word):
            Trie2.path[cur] -= 1
            index = ord(val) - ord("a")
            if Trie2.path[cur] == 0:
                Trie2.tree[cur][index] = 0
                return
            cur = Trie2.tree[cur][index]
        Trie2.end[cur] -= 0

tree = Trie2()
tree.insert("keos")
tree.erase("keos")
print(tree.countWordsStartingWith("keo"))







