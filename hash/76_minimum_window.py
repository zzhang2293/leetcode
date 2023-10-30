class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s = "ADOBECODEBANC", t = "ABC"
        t_table, count, min_window, min_left, min_right = {}, 0, None, None, None
        for c in t:
            t_table[c] = t_table.get(c, 0) + 1
            count += 1
        left, right = 0, 0
        while right < len(s):
            if s[right] in t_table:
                if t_table[s[right]] > 0:
                    count -= 1
                t_table[s[right]] -= 1
                
                if count == 0:
                    while left <= right and (s[left] not in t_table or t_table[s[left]] < 0):
                        if s[left] in t_table:
                            t_table[s[left]] += 1
                        left += 1
                    if min_window == None or min_window > right - left + 1:
                        min_window = right - left + 1
                        min_left = left
                        min_right = right
            right += 1
        if min_window == None:
            return ""
        return s[int(min_left), int(min_right + 1)]
                    
                