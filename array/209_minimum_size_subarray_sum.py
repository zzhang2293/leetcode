class Solution(object):
    def minSubArrayLen(self, target:int, nums:list[int])-> int:
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = 0
        length = len(nums)
        total = 0
        minimum = None
        while right < length:
            total += nums[right]
            current = right - left + 1
            if total >= target:
                while total - nums[left] >= target:
                    total -= nums[left]
                    left += 1
                    current -= 1
                if minimum is None or minimum > current:
                    minimum = current
            right += 1
        return (0 if minimum is None else minimum)
    

obj = Solution()
res = obj.minSubArrayLen(11, [1,2,3,4,5])
print(res)