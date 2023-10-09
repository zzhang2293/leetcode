class MoveZero(object):
    def move_zeros(self, nums:list[int]) :
        upper = 0
        lower = 0
        orig_length = len(nums)
        length = len(nums)
        while upper < orig_length:
            if nums[upper] == 0:
               length -= 1
               upper += 1    # can be more clear or short, but this is for readability
               
            elif nums[upper] != 0:
                if upper != lower:
                    nums[lower] = nums[upper]
                upper += 1
                lower += 1

        nums[:] = nums[:length] + [0] * (orig_length - length)           
        

obj = MoveZero()
nums = [0,1,2,0,3,4]
obj.move_zeros(nums)
print(nums)