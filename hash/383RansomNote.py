#https://leetcode.cn/problems/ransom-note/
class Solution(object):
    def canConstruct(self, ransomNote:str, magazine:str) -> bool:
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_dict = [0] * 26
        for i in range(len(magazine)):
            hash_dict[ord(magazine[i]) - ord("a")] += 1
        for i in range(len(ransomNote)):
            hash_dict[ord(ransomNote[i]) - ord("a")] -= 1
        for val in hash_dict:
            if val < 0:
                return False
        return True