class Solution(object):
    def search(self, nums:list, target:int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # 4 5 6 7 0 1 2 
        
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] == target:
                return mid
            else:
                if nums[left] <= nums[mid]:
                    if target > nums[mid] or target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                    mid = (left + right) // 2
                elif nums[right] >= nums[mid]:
                    if target > nums[right] or target < nums[mid]:
                        right = mid - 1
                    
                    else:
                        left = mid + 1
                    mid = (left + right) // 2
        return -1
    
obj = Solution()
print(obj.search([3, 1], 0))
        