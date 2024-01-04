class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        row, col = len(dp), len(dp[0])
        for j in range(len(s) + 1):
            dp[-1][j] = 1
        for j in range(col - 2, -1, -1):
            for i in range(row - 2, -1, -1):
                dp[i][j] = dp[i][j + 1]
                if s[j] == t[i]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]

