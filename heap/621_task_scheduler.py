from collections import Counter, deque
from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        queue = deque()
        heapq.heapify(max_heap)
        total = 0
        while max_heap or queue:
            total += 1
            if max_heap:
                cur = 1 + heapq.heappop(max_heap)
                if cur:
                    queue.append([cur, total + n])
            if queue and queue[0][1] == total:
                heapq.heappush(max_heap, queue.popleft()[0])
        return total
