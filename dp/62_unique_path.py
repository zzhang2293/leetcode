class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(len(dp[0])):
            dp[-1][i] = 1
        for i in range(len(dp)):
            dp[i][-1] = 1
        row, col = len(dp), len(dp[0])
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]


print(Solution().uniquePaths(3, 7))
