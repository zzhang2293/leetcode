"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        record, cur = {}, head
        while cur:
            record[cur] = Node(x=cur.val)
            cur = cur.next
            
        for item in record:
            record[item].next = record[item.next] if item.next else None
            record[item].random = record[item.random] if item.random else None
        return record[head]
            
        

        