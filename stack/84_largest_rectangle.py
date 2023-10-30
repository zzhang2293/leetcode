# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution(object):
    def largestRectangleArea(self, heights:list):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        max_area, stack = 0, []
        for index, val in enumerate(heights):
            if not stack or stack[-1][1] <= val:
                stack.append([index, val])
            else:
                while stack and stack[-1][1] > val:
                    max_area = max(max_area, (index - stack[-1][0]) * stack[-1][1])
                    last_one = stack.pop()
                stack.append([last_one[0], val])
        for item in stack:
            max_area = max(max_area, (len(heights) - item[0]) * item[1])
        return max_area
            
        
obj = Solution()
print(obj.largestRectangleArea([0, 0]))