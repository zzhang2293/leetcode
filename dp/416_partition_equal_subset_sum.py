from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        reach = sum(nums)
        if reach % 2 != 0: return False
        dp = [[False] * (reach // 2 + 1)for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(dp[0])):
            for j in range(1, len(dp)):
                dp[j][i] = dp[j - 1][i]
                if i >= nums[j - 1]:
                    dp[j][i] = dp[j][i] or dp[j - 1][i - nums[j - 1]]
        return dp[-1][-1]



print(Solution().canPartition([1, 2, 3]))

        


