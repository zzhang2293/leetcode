class Solution(object):
    def carFleet(self, target:int, position:list, speed:list):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        groups = []
        for index in range(len(position)):
            groups.append([position[index], speed[index]])
        groups.sort(key=lambda x : x[0], reverse=True)
        stack = []
        for index, val in enumerate(groups):
            if not stack or (target - val[0]) / val[1] > (target - stack[-1][0]) / stack[-1][1]:
                stack.append(val)
            elif (target - val[0]) / val[1] <= (target - stack[-1][0]) / stack[-1][1]:
                continue
        return len(stack)
    
    
obj = Solution()
res = obj.carFleet(10, [0,4, 2], [2,1, 3])  
print(res)
        
        
        
        