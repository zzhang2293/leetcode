class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = [0] * (len(nums) * 2)
        left, right = 0, len(nums)
        for index in range(len(nums)):
            res[left] = res[right] = nums[index]
            left += 1
            right += 1
        return res

        