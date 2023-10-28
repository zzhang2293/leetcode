# https://leetcode.cn/problems/reverse-string-ii/

class Solution(object):
    def reverseStr(self, s:str, k:int):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        left, right = 0, 0
        length = len(s)
        while length > 0:
            if length > k:
                right = left + k - 1
                temp_left, temp_right = left, right
                while (temp_left < temp_right):
                    #swap
                    temp = s[temp_left] 
                    s[temp_left] = s[temp_right]
                    s[temp_right] = temp
                    temp_left += 1
                    temp_right -= 1 
            elif length <= k:
                right = len(s) - 1
                temp_left, temp_right = left, right
                while (temp_left < temp_right):
                    #swap
                    temp = s[temp_left] 
                    s[temp_left] = s[temp_right]
                    s[temp_right] = temp
                    temp_left += 1
                    temp_right -= 1 

            left = right + k + 1
            length -= 2 * k
        s = "".join(s)
        return s

obj = Solution()
res = obj.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39)
print(res)
            
                
                    
 