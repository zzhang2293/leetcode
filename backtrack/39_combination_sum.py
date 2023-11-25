from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int):
            if i == len(candidates): return
            if sum(subset) > target: return
            if sum(subset) == target:
                res.append(subset.copy())
                return
            subset.append(candidates[i])
            dfs(i)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

obj = Solution()
val = obj.combinationSum([2, 3, 6, 7], 7)
print(val)