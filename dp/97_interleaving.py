class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True
        row, col = len(dp), len(dp[0])
        for i in range(col - 2, -1, -1):
            if s2[i] == s3[i + len(s1)] and dp[-1][i + 1]:
                dp[-1][i] = True
        for i in range(row - 2, -1, -1):
            if s1[i] == s3[i + len(s2)] and dp[i + 1][-1]:
                dp[i][-1] = True
        for j in range(col - 2, -1, -1):
            for i in range(row - 2, -1, -1):
                if s3[i + j] == s1[i] and s3[i + j] == s2[j]:
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
                elif s3[i + j] == s1[i]:
                    dp[i][j] = dp[i + 1][j]
                elif s3[i + j] == s2[j]:
                    dp[i][j] = dp[i][j + 1]
        return dp[0][0]


print(Solution().isInterleave("", "", "a"))
