class MinHeap:
    def __init__(self, capacity:int) -> None:
        self.lst = [0] * capacity
        self.capacity = capacity
        self.size = 0
    
    
    def getParentIndex(self, index:int) -> int:
        return (index - 1) // 2
    
    def getLeftChild(self, index:int) -> int:
        return index * 2 + 1
    
    def getRightChild(self, index:int) -> int:
        return index * 2 + 2
    
    def hasParent(self, index:int) -> bool:
        return self.getParentIndex(index) >= 0
    
    def hasLeftChildren(self, index:int) -> bool:
        return self.getLeftChild(index) < self.size
    
    def hasRightChildren(self, index:int) -> bool:
        return self.getRightChild(index) < self.size
    
    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def swap(self, index1:int, index2:int) -> None:
        self.lst[index1], self.lst[index2] = self.lst[index2], self.lst[index1]
        return
    
    def insert(self, data:int):
        if self.isFull():
            raise("heap is full")
        self.lst[self.size] = data
        self.size += 1

        def up(index:int):
            while self.hasParent(index):
                parent_idx = self.getParentIndex(index)
                if self.lst[index] < self.lst[parent_idx]:
                    self.swap(index, parent_idx)
                    index = parent_idx
                else:
                    break
        up(self.size - 1)
        return
    
    def popMin(self):
        if self.isEmpty():
            raise("is empty heap")
        res = self.lst[0]
        self.lst[0] = self.lst[self.size - 1]
        self.lst[self.size - 1] = 0
        self.size -= 1
        
        def down(index):
            
            while self.hasLeftChildren(index) or self.hasRightChildren(index):
                child = None
                if self.hasLeftChildren(index) and self.hasRightChildren(index):
                    child = (self.getLeftChild(index) if self.lst[self.getLeftChild(index)] < self.lst[self.getRightChild(index)] 
                             else self.getRightChild(index))
                                         
                elif self.hasLeftChildren(index):
                    child = self.getLeftChild(index)
                elif self.hasRightChildren(index):
                    child = self.getRightChild(index)
                
                if self.lst[child] < self.lst[index]:
                    self.swap(child, index)
                else:
                    break
                index = child
        
        down(0)
        return res
    
    def getMin(self):
        if self.isEmpty():
            raise("is empty")
        return self.lst[0]
    
    
    
heap = MinHeap(10)

heap.insert(4)
heap.insert(2)
heap.insert(5)
heap.insert(1)
heap.insert(3)
heap.insert(10)
heap.insert(9)
heap.insert(6)
heap.insert(14)
heap.insert(20)

print(heap.lst)

while not heap.isEmpty():
    print(heap.popMin())
    
    
        
    
    
        