from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            jump_range = nums[i]
            min_step = float("infinity")
            for j in range(i + 1, i + jump_range + 1):
                if j >= len(dp): break
                min_step = min(min_step, dp[j])
            dp[i] = min_step + 1
        return dp[0]


print(Solution().jump([1,1,1,1]))
