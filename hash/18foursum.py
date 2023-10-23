#https://leetcode.cn/problems/4sum/


class Solution(object):
    def fourSum(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for outer_index, outer_val in enumerate(nums):
            if outer_index > 0 and nums[outer_index] == nums[outer_index - 1]:
                continue
            sub_lst = nums[outer_index+1:]
            for inner_index, inner_val in enumerate(sub_lst):
                if inner_index > 0 and sub_lst[inner_index] == sub_lst[inner_index -1]:
                    continue  # i do not want any replication
                left, right = inner_index + 1, len(sub_lst) - 1
                while (left < right):
                    if sub_lst[left] + sub_lst[right] + inner_val + outer_val > target:
                        right -= 1
                    elif sub_lst[left] + sub_lst[right] + inner_val + outer_val < target:
                        left += 1
                    elif sub_lst[left] + sub_lst[right] + inner_val + outer_val == target:
                        # appending the value
                        res.append([outer_val, inner_val, sub_lst[left], sub_lst[right]])
                        left += 1
                        while (left < right and sub_lst[left - 1] == sub_lst[left]):
                            left += 1
        return res
    

obj = Solution()
val = obj.fourSum([1,0,-1,0,-2,2], 0)
print(val)
                        




