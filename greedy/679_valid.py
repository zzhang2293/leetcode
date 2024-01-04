class Solution:
    def checkValidString(self, s: str) -> bool:
        num_rep = []
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                if not stack and not num_rep: return False
                if not stack and len(num_rep) >= 0:
                    num_rep.pop(0)
                if stack: stack.pop(-1)
            elif s[i] == "*":
                num_rep.append(i)
            elif s[i] == "(":
                stack.append(i)

        if len(stack) == 0: return True
        stack_ptr, num_rep_ptr = len(stack) - 1, len(num_rep) - 1
        while stack_ptr >= 0 and num_rep_ptr >= 0:
            if stack[stack_ptr] < num_rep[num_rep_ptr]:
                stack_ptr -= 1
                num_rep_ptr -= 1
            elif stack[stack_ptr] > num_rep[num_rep_ptr]: return False
        if stack_ptr >= 0: return False
        return True

Solution().checkValidString("()(())(((((()())(()))))()(*()))()()()()((()(())())*((((())))*())()(()()))*((()(()(()))))(()())(*(*")