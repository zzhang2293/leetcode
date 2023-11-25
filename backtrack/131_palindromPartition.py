from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def tracking(ptr: int):
            if ptr >= len(s):
                res.append(part.copy())
                return

            for i in range(ptr, len(s)):
                if self.is_palindrome(s, ptr, i):
                    part.append(s[ptr: i + 1])
                    tracking(i + 1)
                    part.pop()
            return

        tracking(0)
        return res

    def is_palindrome(self, s: str, i: int, j: int):
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True


obj = Solution()
print(obj.partition("aa"))
