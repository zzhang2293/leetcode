#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums:list):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0
        for val in nums:
            # check if it is the start 
            if val - 1 not in num_set:
                temp = 1
                temp_val = val
                while temp_val + 1 in num_set:
                    temp += 1 
                    temp_val += 1
                longest = max(longest, temp)

        return longest
        