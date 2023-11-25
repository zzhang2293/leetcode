import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, -num)
            popped = heapq.heappop(self.left)
            heapq.heappush(self.right, -popped)
        else:
            heapq.heappush(self.left, -num)
            popped = heapq.heappop(self.left)
            heapq.heappush(self.right, -popped)
            popped = heapq.heappop(self.right)
            heapq.heappush(self.left, -popped)
        return

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return self.right[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()i
