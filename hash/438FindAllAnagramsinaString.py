#https://leetcode.cn/problems/find-all-anagrams-in-a-string/

"""
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

from collections import Counter


class Solution(object):
    def findAnagrams(self, s:str, p:str) -> list:
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        record = [0] * 26
        res = []
        need, left, right = 0, 0, 0
        for i in range(len(p)):
            record[ord(p[i]) - ord("a")] += 1
            record[ord(s[i]) - ord("a")] -= 1
            right += 1
        diff = [c != 0 for c in record].count(True)
        if diff == 0:
            res.append(0)
        while right < len(s):
            print(s[left: right+1])  #cbaebabacd
            if record[ord(s[right]) - ord("a")] == 0:   
                diff += 1
            elif record[ord(s[right]) - ord("a")] == 1:
                diff -= 1
            record[ord(s[right]) - ord("a")] -= 1
            right += 1
            if record[ord(s[left]) - ord("a")] == -1:
                diff -= 1
            elif record[ord(s[left]) - ord("a")] == 0:
                diff += 1
            record[ord(s[left]) - ord("a")] += 1
            left += 1
            if diff == 0:
                res.append(left)

        return res
    
obj = Solution()
res = obj.findAnagrams("cbaebabacd", "abc")
print(res)

