class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        row, col = len(dp), len(dp[0])
        for i in range(row - 1, -1, -1):
            dp[i][-1] = row - i - 1
        for i in range(col - 1, -1, -1):
            dp[-1][i] = col - i - 1

        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                if word2[i] == word1[j]:
                    dp[i][j] = min(min(dp[i + 1][j], dp[i][j + 1]), dp[i + 1][j + 1])
                else:
                    dp[i][j] = min(min(dp[i + 1][j], dp[i][j + 1]), dp[i + 1][j + 1]) + 1
        return dp[0][0]


print(Solution().minDistance("horse", "ros"))


