class ValidPerfectSquare(object):

    """
        give a num, detect if that is a valid square
    """
    def is_perfect_square(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > num:
                # go left
                right = mid - 1
            
            elif mid * mid < num:
                # go right
                left = mid + 1

            elif mid * mid == num:
                return True
            
        return False
    

obj = ValidPerfectSquare()
ans = obj.is_perfect_square(16)
print(ans)