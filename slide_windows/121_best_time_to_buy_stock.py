# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1
        max_profit = float("-infinity")
        while right < len(prices):
            cur_profit = prices[right] - prices[left]
            max_profit = max(max_profit, cur_profit)
            
            if cur_profit <= 0 :
                left = right
                right += 1
            elif cur_profit > 0:
                right += 1
            
        return max(0, max_profit)
    
    
obj = Solution()
print(obj.maxProfit([2,1,2,1,0,1,2]))