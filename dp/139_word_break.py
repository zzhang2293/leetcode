from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lst = [False] * (len(s) + 1)
        lst[-1] = True
        for i in range(len(lst) - 2, -1, -1):
            for word in wordDict:
                len_word = len(word)
                end = i + len_word - 1
                if end >= len(s): continue
                if s[i: end + 1] == word:
                    lst[i] = True and lst[end + 1]
        return lst[0]


print(Solution().wordBreak("cars", ["car", "ca", "rs"]))
