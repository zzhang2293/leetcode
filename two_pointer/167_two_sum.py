# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution(object):
    def twoSum(self, numbers:list, target:int):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            elif numbers[left] + numbers[right] > target:
                right -= 1
                
            elif numbers[left] + numbers[right] < target:
                left += 1
        return []
        