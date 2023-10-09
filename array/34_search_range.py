class SearchRange(object):
    def searchRange(self, nums:list[int], target: int) -> list[int]:
        # search left range
        left = self.search_left(nums, target)
        right = self.search_right(nums, target)
        if left == -2 and right == -2:
            return [-1, -1]
        
        return [left, right]
    
    def search_left(self, nums:list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        left_border = -2
        while left <= right :    # make the while loop legal
            mid = (left + right) // 2     # at the middle
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target: # in this case, mid pointer will go to left
                right = mid - 1
                if nums[mid] == target:
                    left_border = mid
        return left_border
        
    def search_right(self, nums:list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        right_border = -2

        while left <= right:  # keep the while loop legal
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            
            elif nums[mid] <= target:
                left = mid + 1
                if nums[mid] == target:
                    right_border = mid
        
        return right_border
                

search = SearchRange()
ans = search.searchRange([1,2,3,3,3,3,3,3,4,5], 3)
print(ans)