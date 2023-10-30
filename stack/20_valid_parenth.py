# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        
        record = {")": "(", "]": "[", "}": "{"}
        
        stack = []
        for c in s:
            if c in record:
                if stack and stack[-1] == record[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        if not stack:
            return True
        
        return False
    
        