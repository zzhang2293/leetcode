# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, start: ListNode, end: ListNode):
        pre = None
        end_nxt = end.next
        while start != end_nxt:
            tmp_nxt = start.next
            start.next = pre
            pre = start
            start = tmp_nxt
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy
        start = head
        while True:
            end = pre
            do_it = True
            for i in range(k):
                if end.next is None:
                    do_it = False
                    break
                end = end.next
            if not do_it: break
            end_next = end.next
            tmp_head = self.reverse_list(start, end)
            pre.next = tmp_head
            start.next = end_next
            pre = start
            start = start.next

        return dummy.next


head = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
n = Solution().reverseKGroup(head, 2)
while n:
    print(n.val)
    n = n.next

