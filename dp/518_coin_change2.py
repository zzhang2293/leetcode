from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        row, col = len(dp), len(dp[0])
        for i in range(row):
            dp[i][0] = 1
        for j in range(1, col):
            for i in range(1, row):
                dp[i][j] += dp[i - 1][j]
                if coins[i - 1] <= j:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        return dp[-1][-1]


print(Solution().change(5, [1, 2, 5]))
