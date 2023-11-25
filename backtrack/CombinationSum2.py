from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(ptr: int, sub: list):
            if sum(sub) > target:
                return
            if sum(sub) == target:
                res.append(sub)
                return
            if ptr == len(candidates):
                return
            cur = candidates[ptr]
            ptr += 1
            backtrack(ptr, sub + [cur])

            while ptr < len(candidates) and cur == candidates[ptr]: ptr += 1
            backtrack(ptr, sub)
            return

        backtrack(0, [])
        return res


obj = Solution()
print(obj.combinationSum2([2, 5, 2, 1, 2], 5))
