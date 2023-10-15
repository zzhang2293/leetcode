#https://leetcode.cn/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s:str, t:str):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        
        record = [0] * 26
        for i in range(len(s)):
            record[ord(s[i]) - ord("a")] += 1

        for i in range(len(t)):
            record[ord[s[i]] - ord["a"]] -= 1

        for val in record:
            if val != 0:
                return False
        
        return True

