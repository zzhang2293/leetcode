from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key = (1, buying) val = max_profit

        def dfs(i: int, buying: bool):
            if i >= len(prices): return 0
            if (i, buying) in dp: return dp[(i, buying)]
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            if not buying:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, True)
                dfs[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)
