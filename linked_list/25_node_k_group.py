class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        remain, cur = 0, head
        dummy = ListNode(next=head)
        res = head.next
        pre, cur = dummy, head
        while cur:
            remain += 1
            cur = cur.next
        cur = head
        while remain >= k:
            change = k 
            h = cur
            while change:
                change -= 1
                nxt = cur.next 
                cur.next = pre
                pre = cur
                cur = nxt
            h.next = cur
            change = k
            while dummy.next:
                print(dummy.next.val)
                dummy = dummy.next
            remain -= k
        head = res
            
node = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
obj = Solution()
obj.reverseKGroup(node, 2)
while node:
    print(node.val)
    node = node