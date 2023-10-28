# https://leetcode.cn/problems/reverse-string/
class Solution(object):
    def reverseString(self, s: list[str]):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        left, right = 0, len(s) - 1
        while (left < right):
            left_val = s[left]
            s[left] = s[right]
            s[right] = left_val
            left += 1
            right -= 1
        
