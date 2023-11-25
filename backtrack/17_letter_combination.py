from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        mapper = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        res = []
        cur = []

        def backtracking(ptr: int):
            if ptr >= len(digits):
                s = "".join(cur)
                res.append(s)
                return
            for val in mapper[digits[ptr]]:
                cur.append(val)
                backtracking(ptr + 1)
                cur.pop()
            return
        backtracking(0)
        return res


ob = Solution()
ob.letterCombinations("23")