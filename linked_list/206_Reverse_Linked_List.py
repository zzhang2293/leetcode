#https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# dummy, 1, 2, 3, 4   -> 4, 3, 2, 1, dummy
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev
            
             
            