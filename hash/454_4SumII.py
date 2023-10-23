#https://leetcode.cn/problems/4sum-ii/

class Solution(object):
    def fourSumCount(self, nums1:list, nums2:list, nums3:list, nums4:list) -> int:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = 0
        mapping = dict()
        for val1 in nums1:
            for val2 in nums2:
                mapping[val1 + val2] = mapping.get(val1+val2, 0) + 1
        for val3 in nums3:
            for val4 in nums4:
                if 0 - val3 - val4 in list(mapping.keys()):
                    count += mapping[0 - val3 - val4]
        return count
    

obj = Solution()
res = obj.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])
print(res)