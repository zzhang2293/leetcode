#https://leetcode.cn/problems/intersection-of-two-arrays-ii/
class Solution(object):
    def intersect(self, nums1:str, nums2:str) -> list:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        lookup = {}
        for val in nums1:
            lookup[val] = lookup.get(val, 0) + 1
        res = []
        for val in nums2:
            if val in list(lookup.keys()) and lookup[val] > 0:
                res.append(val)
                lookup[val] -= 1
        return res
