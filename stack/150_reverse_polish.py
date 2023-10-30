# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens:list[str]):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        '''
            2, 1, +, 3, *
            (2 + 1) * 3
        '''
        
        stack = []
        for val in tokens:
            if self.check_digit(val):
                stack.append(val)
            else:
                num1 = int(stack.pop())
                num2 = int (stack.pop())
                if val == '+':
                    new_num = num2 + num1
                elif val == '-':
                    new_num = num2 - num1
                elif val == '*':
                    new_num = num2 * num1
                elif val == '/':
                    new_num = int(float(num2) / num1)
                    
                stack.append(new_num)
        return int(stack[-1])
    
    def check_digit(self, num:str):
        try:
            int(num)
            return True
        except ValueError:
            return False
obj = Solution()
print(obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
))