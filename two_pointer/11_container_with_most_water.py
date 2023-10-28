# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height:list):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        
        maximum = 0
        while left < right:
            vol = (right - left) * min(height[left], height[right])
            maximum = max(maximum, vol)
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        return maximum