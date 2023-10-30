# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # A A B A A
        left, right = 0, 0
        record = [0] * 26
        res = 0
        while right < len(s):
            record[ord(s[right]) - ord("A")] += 1
            total_char = 0
            largest_char = None
            for val in record:
                largest_char = val if largest_char == None else max(largest_char, val)
                total_char += val if val != 0 else 0
            while total_char - largest_char > k:
                record[ord(s[left]) - ord("A")] -= 1
                left += 1
                total_char = 0
                largest_char = None
                for val in record:
                    largest_char = val if largest_char == None else max(largest_char, val)
                    total_char += val if val != 0 else 0
            res = max(res, right - left + 1)
            right += 1
        return res
        
    
obj = Solution()
print(obj.characterReplacement("ABCCSSMESS", 2))
