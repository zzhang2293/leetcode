class Solution(object):
    def sortedSquares(self, nums:list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] ** 2 >= nums[right] ** 2:
                res.insert(0, nums[left] ** 2)
                left += 1
            else:
                res.insert(0, nums[right] ** 2)
                right -= 1

        return res
    

obj = Solution()
res = obj.sortedSquares([-5, -2, 0, 1, 2, 3])
print(res)


        
