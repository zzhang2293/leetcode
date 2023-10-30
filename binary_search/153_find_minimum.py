# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums:list):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6, 7, 0, 1, 2, 3, 4, 5, 5,
        left, right = 0, len(nums) - 1
        
        mid = (left + right) // 2
        res = nums[mid]
        while nums[left] > nums[right]:
            if nums[mid] >= nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1
            mid = (left + right) // 2
            res = min(res, nums[mid])
        return min(res, nums[left])
    
obj = Solution()
print(obj.findMin([3, 1, 2]))