from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}

        def dfs(ptr: int, is_even: bool):
            if ptr >= len(nums): return 0
            if (ptr, is_even) in dp: return dp[(ptr, is_even)]
            total = nums[ptr] if is_even else -nums[ptr]
            dp[(ptr, is_even)] = max(total + dfs(ptr + 1, not is_even), dfs(ptr + 1, is_even))
            return dp[(ptr, is_even)]

        return dfs(0, True)





