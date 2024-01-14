class ChainForwardStar:
    N = 10
    head = [0] * N
    nxt = [0] * N
    to = [0] * N
    weight = [0] * N
    cnt = 1
    amount = 0

    def build(self, n):
        for i in range(self.N):
            self.head[i] = 0
            self.nxt[i] = 0
            self.to[i] = 0
            self.weight[i] = 0
        self.cnt = 1
        self.amount = n

    def construct(self, adj: list) -> None:
        for From, To, Weight in adj:
            give, self.cnt = self.cnt, self.cnt + 1
            self.nxt[give] = self.head[From]
            self.to[give] = To
            self.weight[give] = Weight
            self.head[From] = give
        return

    def __str__(self):
        ans = ""
        for i in range(1, self.amount + 1):
            ans += f"{i} \n"
            cur = self.head[i]
            while cur != 0:
                ans += f"To: {self.to[cur]} Weight: {self.weight[cur]}\n"
                cur = self.nxt[cur]
        return ans


obj = ChainForwardStar()
obj.build(3)
conn = [[1, 2, 2], [1, 3, 1], [2, 3, 1], [3, 2, 1]]
obj.construct(conn)
print(obj)
