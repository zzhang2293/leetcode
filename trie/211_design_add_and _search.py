class Node:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.root)
    def searchHelper(self, word:str, root:Node) -> bool:
        if len(word) == 0:
            return root.end_of_word
        c = word[0]
        if c != '.':
            if c in root.children:
                return self.searchHelper(word[1:], root.children[c])
            else:
                return False
        else:
            if root.children:
                contain = False
                for element in root.children:
                    contain = contain or self.searchHelper(word[1:], root.children[element])
                return contain
            else:
                return False