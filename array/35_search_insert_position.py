class SearchInsertPosition(object):
    def searchInsert(self, nums: list[int],target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            if nums[mid] > target:
                # go to left
                right = mid - 1
            elif nums[mid] < target:
                # go to right
                left = mid + 1
            elif nums[mid] == target:
                return mid
        
            mid = (left + right) // 2
        
        
        return left

b = SearchInsertPosition()
res = b.searchInsert([3,4,5,6,7], 8 )
print(res)