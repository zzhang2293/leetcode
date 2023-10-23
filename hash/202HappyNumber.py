#https://leetcode.cn/problems/happy-number/
class Solution(object):
    def isHappy(self, n:int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        exist = set()
        while n != 1:
            if n in exist:
                return False
            exist.add(n)
            n = self.cal(n)
            
        return True
        

    def cal(self, n:int) -> int:
        total = 0
        while n > 0 :
            n, r = divmod(n, 10)    # n / 10 = n .... r
            total += r ** 2
        return total
    

obj = Solution()
res = obj.isHappy(19)
print(res)