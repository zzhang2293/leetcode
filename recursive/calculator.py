class Solution:
    def calculate(self, s: str) -> int:
        operation = ["+", "-", "*", "/"]

        def helper(ptr: int):
            cur = 0
            stack_num = []
            stack_oper = []
            while ptr < len(s):
                if s[ptr] in operation:
                    if stack_oper and stack_oper[-1] == "/":
                        stack_oper.pop(-1)
                        popped = stack_num.pop(-1)
                        if popped * cur < 0:
                            cur = -1 * (abs(popped) // abs(cur))
                        else:
                            cur = popped // cur
                    elif stack_oper and stack_oper[-1] == "*":
                        stack_oper.pop(-1)
                        cur = stack_num.pop(-1) * cur
                    stack_num.append(cur)
                    stack_oper.append(s[ptr])
                    cur = 0
                elif s[ptr] == "(":
                    ptr, cur = helper(ptr + 1)
                elif s[ptr] == ")":
                    break
                else:
                    cur = cur * 10 + ord(s[ptr]) - ord("0")
                ptr += 1

            if stack_oper and stack_oper[-1] == "/":
                stack_oper.pop(-1)
                popped = stack_num.pop(-1)
                if popped * cur < 0:
                    cur = -1 * (abs(popped) // abs(cur))
                else:
                    cur = popped // cur
            elif stack_oper and stack_oper[-1] == "*":
                stack_oper.pop(-1)
                cur = stack_num.pop(-1) * cur
            stack_num.append(cur)
            res = stack_num[0]
            for ind in range(1, len(stack_num)):
                if stack_oper[ind - 1] == "+":
                    res += stack_num[ind]
                elif stack_oper[ind - 1] == "-":
                    res -= stack_num[ind]
            return ptr, res

        ind, val = helper(0)
        return int(val)


print(Solution().calculate("3/(2/1-4)"))
