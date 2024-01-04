from typing import List
import heapq

class Solution:

    def cal_distance(self, x1, x2, y1, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dis = self.cal_distance(x1, x2, y1, y2)
                adj[i].append([dis, j])
                adj[j].append([dis, i])

        res = 0
        visited = set()
        min_heap = [[0, 0]] # cost, point
        while len(visited) < n:
            cost, index = heapq.heappop(min_heap)
            if index in visited:
                continue
            res += cost
            visited.add(index)
            for nei_cost, nei in adj[index]:
                if nei not in visited:
                    heapq.heappush(min_heap, [nei_cost, nei])

        return res



print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))




