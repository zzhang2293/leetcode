class UnionFind(object):
    def __init__(self, n):
        self.parent: list = [i for i in range(n)]
        self.size: list = [0 for _ in range(n)]
        self.MAX: int = n
        self.stack: list = []

    def build(self) -> None:
        for i in range(self.MAX):
            self.parent[i] = i
            self.size[i] = 1
        return

    def isSameSet(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def find(self, num: int) -> int:
        while num != self.parent[num]:
            self.stack.append(num)
            num = self.parent[num]
        while self.stack:
            self.parent[self.stack.pop()] = num
        return num

    def union(self, a: int, b: int):
        fa = self.find(a)
        fb = self.find(b)
        if self.size[fa] > self.size[fb]:  # fa is greater
            self.size[fa] += self.size[fb]
            self.parent[fb] = fa
        else:
            self.size[fb] += self.size[fa]
            self.parent[fa] = fb
        return

    def __str__(self):
        return str(self.parent)


obj = UnionFind(10)
obj.build()
print(obj)
obj.union(0, 1)
print(obj)
obj.union(2, 9)
print(obj)
print(obj.find(2))

