from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums))
        dp[-1] = True
        near_true = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= near_true:
                dp[i] = True
                near_true = i
        return dp[0]
