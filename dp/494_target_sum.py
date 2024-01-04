from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(p: int, cur: int):
            if (p, cur) in dp:
                return dp[(p, cur)]
            if p == len(nums) and cur == target:
                dp[(p, cur)] = 1
                return 1
            if p == len(nums) and cur != target:
                return 0
            res = 0
            res += dfs(p + 1, cur + nums[p])
            res += dfs(p + 1, cur - nums[p])
            dp[(p, cur)] = res
            return res

        return dfs(0, 0)


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))

