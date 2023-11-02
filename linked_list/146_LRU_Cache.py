class Node:
    
    def __init__(self, key:int, val:int, ) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache, self.capacity = {}, capacity
        self.least_use, self.most_use = Node(0, 0), Node(0, 0)
        self.least_use.prev, self.most_use.next = self.most_use, self.least_use
        


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node:Node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
    
    # remove from the list
    def remove(self, node:Node):
        pre:Node = node.prev
        nxt:Node = node.next
        pre.next, nxt.prev = nxt, pre
        del self.cache[node.key]
        
    # insert from the list
    def insert(self, node:Node):
        cur_most = self.most_use.next
        self.most_use.next = node
        node.prev = self.most_use
        node.next = cur_most
        cur_most.prev = node
        self.cache[node.key] = node
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node = Node(key, value)
            self.insert(node)
        else:
            if len(self.cache) < self.capacity:
                node = Node(key, value)
                self.insert(node)
            else:
                removed = self.least_use.prev
                node = Node(key, value)
                self.remove(removed)
                self.insert(node)
                
    def __str__(self) -> str:
        head = self.most_use
        res = ""
        while head:
            res += f"[key: {head.key}, value: {head.val}]\n"
            head = head.next
        return res


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache(1)
cache.put(2, 1)
cache.get(2)
print(cache)