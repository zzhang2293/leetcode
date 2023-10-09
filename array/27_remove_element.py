class RemoveElement(object):
    """
        remove all the target element
    """
    def remove_element(self, nums:list[int], val:int) -> int:
        pointer_quick = 0
        pointer_slow = 0
        length = len(nums)
        res = length
        for _ in range(length):
            if nums[pointer_quick] == val:
                pointer_quick += 1
                res -= 1
                continue
            if pointer_quick != pointer_slow:
                nums[pointer_slow] = nums[pointer_quick]

            pointer_slow += 1
            pointer_quick += 1

        nums = nums[:res]
        return res
    


obj = RemoveElement()
nums = [3,2,2,3]
res = obj.remove_element(nums, 3)
print(res)
print(nums)