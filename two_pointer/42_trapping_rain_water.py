# https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height:list):
        """
        :type height: List[int]
        :rtype: int
        """
        total = 0
        left, right = 0, len(height) - 1
        max_left, max_right = -1, -1
        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if height[left] <= height[right]:
                left += 1
                total += max(min(max_left, max_right) - height[left], 0)
            elif height[left] > height[right]:
                right -= 1
                total += max(min(max_left, max_right) - height[right], 0)
        return total
                        