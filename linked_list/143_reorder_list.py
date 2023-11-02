# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # 1, 2, 3, 4, 5
        # 1, 5, 
        slow = head
        fast:ListNode = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right:ListNode = slow.next
        slow.next = pre = None
        
        while right:
            nxt = right.next
            right.next = pre
            pre = right
            right = nxt
        
        # merge two halfs
        right = pre
        left = head
        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left = temp1
            right = temp2
        
        
        
            
        
            
        
        
        
        
            
        