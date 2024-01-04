from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        lst1 = nums[1:] + [0]
        lst2 = nums[:-1] + [0]
        #[1,2,3,4,1,0]
        for i in range(len(lst1) - 3, -1, -1):
            lst1[i] = max(lst1[i + 1], lst1[i + 2] + lst1[i])
        for i in range(len(lst2) - 3, -1, -1):
            lst2[i] = max(lst2[i + 1], lst2[i + 2] + lst2[i])
        return max(lst1[0], lst2[0])


print(Solution().rob([8, 2, 8, 9 ,2]))
