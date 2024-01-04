class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def helper(ptr: int):
            tmp_table = {}
            nested_table = None
            variable = None
            times = 0
            while ptr < len(formula):
                if ord("a") <= ord(formula[ptr]) <= ord("z"):
                    variable += formula[ptr]
                elif ord("0") <= ord(formula[ptr]) <= ord("9"):
                    times = times * 10 + (ord(formula[ptr]) - ord("0"))
                elif ord("A") <= ord(formula[ptr]) <= ord("Z"):
                    if variable:
                        tmp_table[variable] = tmp_table.get(variable, 0) + max(1, times)
                    if nested_table:
                        for key, val in nested_table.items():
                            tmp_table[key] = tmp_table.get(key, 0) + val * max(1, times)
                        nested_table = None
                    times = 0
                    variable = formula[ptr]
                elif formula[ptr] == "(":
                    if variable:
                        tmp_table[variable] = tmp_table.get(variable, 0) + max(1, times)
                        variable = None
                    if nested_table:
                        for key, val in nested_table.items():
                            tmp_table[key] = tmp_table.get(key, 0) + val * max(1, times)
                        nested_table = None
                    times = 0
                    ptr, nested_table = helper(ptr + 1)
                elif formula[ptr] == ")":
                    break
                ptr += 1
            if variable:
                tmp_table[variable] = tmp_table.get(variable, 0) + max(1, times)
            if nested_table:
                for key, val in nested_table.items():
                    tmp_table[key] = tmp_table.get(key, 0) + val * max(1, times)
            return ptr, tmp_table
        ptr, table = helper(0)
        table = sorted(table.items(), key=lambda x: x[0])
        res = ""
        for key, val in table:
            res += f"{key}{val}" if val > 1 else f"{key}"
        return res


print(Solution().countOfAtoms("Be32"))
