class Solution:
    def countSubstrings(self, s: str) -> int:
        matrix = [[False] * len(s) for _ in range(len(s))]
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
                if (s[start] == s[end]) and matrix[start + 1][end - 1]:
                    matrix[start][end] = True
        res, num = set(), 0
        for cur_len in range(1, len(s) + 1):
            for start in range(0, len(s) - cur_len + 1):
                end = start + cur_len - 1
                if matrix[start][end] and s[start: end + 1]:
                    num += 1
        return num

print(Solution().countSubstrings("aaa"))

