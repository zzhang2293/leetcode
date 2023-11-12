import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = []
        for item in points:
            dis = item[0] ** 2 + item[1] ** 2
            minHeap.append([dis, item[0], item[1]])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            res.append(heapq.heappop(minHeap)[1:])
            k -= 1
            
        return res
            