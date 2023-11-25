from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums.copy()]

        for index in range(len(nums)):
            popped = nums.pop(0)
            permute = self.permute(nums)
            for perm in permute:
                perm.append(popped)
            res.extend(permute)
            nums.append(popped)
        return res


obj = Solution()
print(obj.permute([1, 2, 3]))