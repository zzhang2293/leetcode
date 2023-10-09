from collections import Counter


class Solution(object):
    def totalFruit(self, fruits:list[int]):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # [1,3,2,1,1]
        left = 0
        fruit_hash = Counter()
        maximum = 0
        for right, x in enumerate(fruits):
            fruit_hash[x] += 1
            while len(fruit_hash) > 2:
                fruit_hash[fruits[left]] -= 1
                if fruit_hash[fruits[left]] == 0:
                    fruit_hash.pop(fruits[left])
                left += 1
            maximum = max(maximum, right - left + 1)
        return maximum
    

obj = Solution()
res = obj.totalFruit([1,2,3,2,2,3,4,5,6])
print(res)