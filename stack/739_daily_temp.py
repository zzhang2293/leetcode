# https://leetcode.com/problems/daily-temperatures/
class Solution(object):
    def dailyTemperatures(self, temperatures:list):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        stack, res = [], [0] * len(temperatures)
        
        for index, val in enumerate(temperatures):
            if not stack or temperatures[stack[-1]] > val:
                stack.append(index)
                
            else:
                while stack and temperatures[stack[-1]] < val:
                    day = stack.pop()
                    diff = index - day
                    res[day] = diff
                stack.append(index)
        for day in stack:
            res[day] = 0
        return res
    
obj = Solution()
res = obj.dailyTemperatures([73,74,75,71,69,72,76,73])
print(res)
                    
                