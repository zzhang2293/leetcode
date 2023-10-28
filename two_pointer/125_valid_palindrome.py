# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while r > l and not alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
        return True
            
        
        
    def alphaNum(self, c:str):
    
        return ((ord('A') <= ord(c) <= ord('Z'))
                or (ord('a') <= ord(c) <= ord('z')) 
                or (ord('0') <= ord(c) <= ord (9)))

        
    