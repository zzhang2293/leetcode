#https://leetcode.cn/problems/3sum/

class Solution(object):
    def threeSum(self, nums:list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        right = len(nums) - 1
        for index, val in enumerate(nums):
            if index > 0 and val == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                if val + nums[left] + nums[right] == 0:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif val + nums[left] + nums[right] < 0:
                    left += 1
                elif val + nums[left] + nums[right] > 0:
                    right -= 1
            
        return res
