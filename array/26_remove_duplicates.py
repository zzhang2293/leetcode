class RemoveDuplicates(object):
    def remove_duplicates(self, nums:list[int]) -> int:
        '''
            remove the duplicates in-place each unique element appears onece
        '''
        
        length = len(nums)
        if length == 1 or length == 0:
            return length
        quick = 0
        slow = 0
        alter_len = length
        # [1,2,2,3,4,5,5]
        while quick <= length - 1:
            if quick < (length - 1) and nums[quick] == nums[quick+1]:
                quick += 1
                alter_len -= 1    # i know in this case length will decrease
                continue
            else:
                nums[slow] = nums[quick]

            slow += 1
            quick += 1
        nums[:] = nums[:alter_len]
        return alter_len


obj = RemoveDuplicates()
nums = [1,2,2,2,3,4,5,5,6,6,7]
res = obj.remove_duplicates(nums)
print(res)
print(nums)