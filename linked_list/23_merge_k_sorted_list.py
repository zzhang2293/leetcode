from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        return self.divide(lists)
        
    def divide(self, lists:list[ListNode]):
        if len(lists) == 1:
            return lists[0]
        
        elif len(lists) == 2:
            link1 = lists[0]
            link2 = lists[1]
            return self.conquer(link1, link2)
        else:
            mid = (len(lists) - 1) // 2
            left = self.divide(lists[0:mid+1])
            right = self.divide(lists[mid+1:])
            return self.conquer(left, right)
            
    def conquer(self, link1:ListNode, link2:ListNode):
        res = ListNode()
        res_head = res
        while link1 and link2:
            if link1.val <= link2.val:
                res.next = ListNode(link1.val)
                res = res.next
                link1 = link1.next
            else:
                res.next = ListNode(link2.val)
                res = res.next
                link2 = link2.next
        if link1:
            res.next = link1
        if link2:
            res.next = link2
        return res_head.next
    
node1 = ListNode(1, ListNode(4, ListNode(5)))
node2 = ListNode(2, ListNode(3, ListNode(4)))
node3 = ListNode(2, ListNode(6))

lst = [node1, node2, node3]
obj = Solution()
node = obj.mergeKLists(lst)

while node:
    print(node.val)
    node = node.next
        