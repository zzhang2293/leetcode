class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0
        record = set()
        while right < len(s):
            if s[right] not in record:
                record.add(s[right])
                max_len = max(max_len, right - left + 1)
            elif s[right] in record:
                while s[left] != s[right]:
                    record.remove(s[left])
                    left += 1
                
                left += 1
                
            right += 1
        return max_len
                    
obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))