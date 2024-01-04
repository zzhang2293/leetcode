from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i + 1], nums[i + 2] + nums[i])

        return nums[0]


print(Solution().rob([1,2,3,1]))