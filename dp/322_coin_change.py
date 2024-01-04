from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        lst = [float("infinity")] * (amount + 1)
        lst[0] = 0
        for i in range(1, len(lst)):
            for value in coins:
                if i - value >= 0:
                    lst[i] = min(lst[i], 1 + lst[i - value])
        return int(lst[-1]) if lst[-1] != float("infinity") else -1


print(Solution().coinChange([1,2,3,4,6], 12313442))
