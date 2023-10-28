#https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        record = [[] for i in range(len(nums) + 1)]
        mapping = {}
        for index, val in enumerate(nums):
            mapping[val] = mapping.get(val, 0) + 1
        for index, val in mapping.items():
            record[val].append(index)
        for index in range(len(record) - 1, 0, -1):
            if record[index] != []:
                if k <= 0:
                    break
                k -= len(record[index])
                for v in record[index]:
                    res.append(v)
        return res
    
obj = Solution()
print(obj.topKFrequent([1], 1))