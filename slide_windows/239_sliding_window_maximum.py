class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = []
        res = []
        left, right = 0, k - 1
        for index in range(right + 1):
            if not queue or queue[-1] >= nums[index]:
                queue.append(nums[index])
            else:
                while queue and queue[-1] < nums[index]:
                    queue.pop()
                queue.append(nums[index])
        res.append(queue[0])
        right += 1
        while right < len(nums):
            if not queue or queue[-1] >= nums[right]:
                queue.append(nums[right])
            else:
                while queue and queue[-1] < nums[right]:
                    queue.pop()
                queue.append(nums[right])
                
            if nums[left] == queue[0]:
                queue.remove(nums[left])
            left += 1
            res.append(queue[0])
            right += 1
        return res
    
obj = Solution()
print(obj.maxSlidingWindow([1, -1], 1))