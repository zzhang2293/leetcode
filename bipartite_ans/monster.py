def min_round(poison: list, atteck: list, hp: int):

    def helper(r: int):
        ans = 0
        for i in range(r):
            ans += max(poison[i] * (r - i - 2), atteck[i])
        return ans

    l, r = 0, 0



