from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for time in times:
            adj[time[0]].append(time[1:])
        res = 0
        heap, visited = [[0, k]], set()
        while len(visited) < n:
            if not heap: return -1
            popped_dis, popped_val = heapq.heappop(heap)
            res = max(res, popped_dis)
            visited.add(popped_val)
            for nei, dis in adj[popped_val]:
                if nei not in visited:
                    heapq.heappush(heap, [popped_dis + dis, nei])
        return res


print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

