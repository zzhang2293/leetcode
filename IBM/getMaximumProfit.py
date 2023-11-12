class Solution:
    # [1,5,3,4,6] [2,3,4,5,6]
    def getMaximumProfit(self, price: list, profit:list):
        # mapping = {}
        max_profit = float("-infinity")
        def cal(res:list):
            nonlocal max_profit
            if len(res) == 3:
                max_profit =  max(max_profit, profit[res[0]] + profit[res[1]] + profit[res[2]])
                return
            sub_str = price[res[-1]+1:]
            if len(sub_str) == 0:
                return
            for index, val in enumerate(sub_str):
                if val > price[res[-1]]:
                    res.append(index + res[-1] + 1)
                    cal(res)
                    res.pop()
            return

        for index in range(len(price)):
            cal([index])
            
        return max_profit
    
obj = Solution()
res = obj.getMaximumProfit([1,5,3,4,6], [2, 3, 4, 5, 6])
print(res)