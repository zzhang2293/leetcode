from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-infinity")
        dp = [0] * (len(nums) + 1)
        dp[0] = float("-infinity")
        for index, val in enumerate(nums):
            dp[index + 1] = max(dp[index] + nums[index], nums[index])
            res = max(res, dp[index + 1])
        return res
