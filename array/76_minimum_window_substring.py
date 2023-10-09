

class Solution(object):

    """
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
    """
    def minWindow(self, s:str, t:str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        need_count = 0
        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
            need_count += 1
        left = 0
        right = 0
        min_len = None
        
        length = len(s)
        while right < length:
            if s[right] in list(need.keys()):
                need[s[right]] -= 1
                if need[s[right]] >= 0:
                    need_count -= 1
                while True:
                    if s[left] in list(need.keys()):
                        if need[s[left]] < 0:
                            need[s[left]] += 1
                            left += 1
                        else:
                            break
                    elif s[left] not in list(need.keys()):
                        left += 1

                if need_count == 0:
                    if min_len is None or min_len > right - left + 1:
                        min_len = right - left + 1
                        min_left = left
                        min_right = right
            right += 1

        return ("" if min_len is None else s[min_left: min_right + 1])
                



obj = Solution()
res = obj.minWindow("a", "aa")
print(res)
        

        
