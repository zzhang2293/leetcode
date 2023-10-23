#https://leetcode.cn/problems/two-sum/
class Solution(object):
    def twoSum(self, nums: list, target: int) -> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
    
    
obj = Solution()

        