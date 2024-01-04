from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums.append(1)
        nums.insert(0, 1)

        def dfs(l: int, r: int):
            if l > r: return 0
            if (l, r) in dp: return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)


print(Solution().maxCoins([3, 1, 5, 8]))
