class Solution:
    def longestPalindrome(self, s: str) -> str:
        matrix = [[False] * len(s) for _ in range(len(s))]
        max_len, res = 1, s[0]
        # base case 1
        for i in range(len(s)):
            matrix[i][i] = True
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                max_len, res = 2, s[i - 1: i + 1]
                matrix[i - 1][i] = True
        # print(matrix)
        for cur_len in range(3, len(s) + 1):
            for start in range(len(s)):
                end = start + cur_len - 1
                if end >= len(s): break
                cur_res = (s[start] == s[end]) and matrix[start + 1][end - 1]
                if cur_res:
                    matrix[start][end] = True
                    if max_len < cur_len:
                        max_len, res = cur_len, s[start: end + 1]

        return res


print(Solution().longestPalindrome("aaaaa"))

