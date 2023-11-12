import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            smash = stone2 - stone1
            if smash != 0:
                heapq.heappush(smash)
            
        return abs(stones[0]) if stones else 0