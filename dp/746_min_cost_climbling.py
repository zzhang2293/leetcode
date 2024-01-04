from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        dp[-1], dp[-2] = 0, cost[-1]
        #bese case
        for i in range(len(cost) - 2, -1, -1):
            dp[i] = min(dp[i + 1] + cost[i], dp[i + 2] + cost[i])
        return min(dp[0], dp[1])


print(Solution().minCostClimbingStairs([10, 15, 20]))