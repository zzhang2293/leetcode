from typing import List
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mem = [float("infinity")] * n
        mem[src] = 0
        for _ in range(k + 1):
            tmp_mem = mem.copy()
            for start, end, price in flights:
                if mem[start] == float("infinity"): continue
                tmp_mem[end] = min(tmp_mem[end], mem[start] + price)
            mem = tmp_mem.copy()
        return mem[dst] if mem[dst] != float("infinity") else -1



print(Solution().findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1))
