from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(index: int, buying: bool):
            if index >= len(prices): return 0
            if (index, buying) in dp: return dp[(index, buying)]
            if buying:
                buy = dfs(index + 1, not buying) - prices[index]
                freeze = dfs(index + 1, buying)
                dp[(index, buying)] = max(buy, freeze)
            elif not buying:
                sell = dfs(len(prices), not buying) + prices[index]
                freeze = dfs(index + 1, buying)
                dp[(index, buying)] = max(sell, freeze)
            return dp[(index, buying)]

        return dfs(0, True)

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))

