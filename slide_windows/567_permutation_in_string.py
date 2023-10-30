# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1) - 1
        record = {}
        if len(s1) > len(s2):
            return False
        for index, val in enumerate(s1):
            record[val] = record.get(val, 0) + 1
        curr = {} 
        while right < len(s2):
            
            for i in range(left, right+1):
                curr[s2[i]] = curr.get(s2[i], 0) + 1
            same = True
            for key in curr:
                if not key in record or not record[key] == curr[key]:
                    same = False
                    break
            if same:
                return True
            left += 1
            right += 1
            curr.clear()
            
        return False
    
obj = Solution()
print(obj.checkInclusion("ab", "eidboaoo"))