from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(ptr: int, sub: list):
            if ptr == len(nums):
                res.append(sub)
                return
            cur = nums[ptr]
            ptr += 1
            backtrack(ptr, sub + [cur])
            while ptr < len(nums) and cur == nums[ptr]:
                ptr += 1
            backtrack(ptr, sub)
            return

        backtrack(0, [])
        return res


obj = Solution()
print(obj.subsetsWithDup([1,2,2]))