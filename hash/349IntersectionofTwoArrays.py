
#https://leetcode.cn/problems/intersection-of-two-arrays/
class Solution(object):
    def intersection(self, nums1:list, nums2:list) -> list:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)