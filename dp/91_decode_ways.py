class Solution:
    def numDecodings(self, s: str) -> int:
        lst = [0] * (len(s) + 1)
        lst[-1] = 1
        valid = [str(x) for x in range(1, 27)]
        if s[-1] in valid:
            lst[-2] = 1
        for i in range(len(lst) - 3, -1, -1):
            if s[i] in valid:
                lst[i] += lst[i + 1]
            if s[i: i + 2] in valid:
                lst[i] += lst[i + 2]
        return lst[0]
        # print(valid)


print(Solution().numDecodings("0"))