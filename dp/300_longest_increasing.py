from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [[0] * 2 for _ in range(len(nums))]
        if not nums: return 0
        res = 1
        for index, value in enumerate(nums):
            lst[index][0] = value
        lst[0][1] = 1
        for i in range(1, len(lst)):
            max_len = 0
            for j in range(0, i):
                if lst[j][0] < nums[i]:
                    max_len = max(max_len, lst[j][1])
            lst[i][1] = max_len + 1
            res = max(res, max_len + 1)
        return res


print(Solution().lengthOfLIS([1,3,]))
