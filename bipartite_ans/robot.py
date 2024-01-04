def robot(lst: list):
    def helper(initial: int):
        for val in lst:
            if initial > val:
                initial += initial - val
            elif initial <= val:
                initial -= val - initial

            if initial < 0: return False
        return True

    l, r = 0, 0
    for val in lst:
        r = max(r, val)
    res = 0
    while l <= r:
        mid = (l + r) // 2
        if helper(mid):
            r = mid - 1
            res = r
        else:
            l += 1
    return res




def max_len(nums: list):
    def helper(limit: int):
        angry = set()
        res = 0
        table = {}
        r = 0
        for left in range(len(nums)):
            while len(table) <= limit and r < len(nums):
                table[nums[r]] = table.get(nums[r], 0) + 1
                if table[nums[r]] % 2 != 0: angry.add(nums[r])
                else: angry.remove(nums[r])
                if not angry and len(table) == limit: res = max(res, r - left + 1)
                r += 1
            table[nums[left]] -= 1
            if nums[left] in angry and table[nums[left]] % 2 == 0: angry.remove(nums[left])
            elif table[nums[left]] % 2 != 0:
                angry.add(nums[left])
            if table[nums[left]] == 0: del table[nums[left]]
        return res

    ans = 0
    for i in range(1, 27):
        ans = max(ans, helper(i))
    return ans


