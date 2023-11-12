class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        longest_prefix_suffix = [0] * len(needle)
        position, previous_longest_substring = 1, 0
         
        while position < len(needle):
            if needle[position] == needle[previous_longest_substring]:
                longest_prefix_suffix[position] = previous_longest_substring + 1
                previous_longest_substring += 1
                position += 1
            elif previous_longest_substring == 0:
                longest_prefix_suffix[position]= 0
                position += 1
            else:
                previous_longest_substring = longest_prefix_suffix[previous_longest_substring - 1]
            
            
            haystack_pointer, needle_pointer = 0, 0
            
        while haystack_pointer < len(haystack):
            if haystack[haystack_pointer] == needle[needle_pointer]:
                haystack_pointer += 1
                needle_pointer += 1
            elif needle_pointer != 0:
                needle_pointer = longest_prefix_suffix[needle_pointer - 1]
            
            elif needle_pointer == 0:
                haystack_pointer += 1
            
            if needle_pointer == len(needle):
                return haystack_pointer - needle_pointer
            
        return -1
                
obj = Solution()
obj.strStr("A", "A")