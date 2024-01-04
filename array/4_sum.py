from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums4_set = {}
        for i in nums4:
            for j in nums3:
                nums4_set[i + j] = nums4_set.get(i + j, 0) + 1

        val = 0
        for i in nums1:
            for j in nums2:
                val += nums4_set.get(-(i + j), 0)
        return val


print(Solution().fourSumCount([0, 1, -1], [-1, 1, 0], [0, 0, 1], [-1, 1, 1]))
