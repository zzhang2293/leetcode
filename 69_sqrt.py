class Sqrt(object):
    def my_sqrt(self, x:int) -> int:
        nums = list(range(0, x + 1))
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] * nums[mid] <= x:
                ans = mid
                left = mid + 1
            
            elif nums[mid] * nums[mid] > x:
                right = mid - 1

        return ans