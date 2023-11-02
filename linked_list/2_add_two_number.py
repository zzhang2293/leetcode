# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2, bit1, bit2 = 0, 0, 1, 1
        while l1:
            num1 += l1.val * bit1
            bit1 *= 10
            l1 = l1.next
        while l2:
            num2 += l2.val * bit2
            bit2 *= 10
            l2 = l2.next
        res_num = num1 + num2
        res_num = str(res_num)
        res = ListNode()
        res_head = res
        for index, val in reversed(list(enumerate(res_num))):
            res.next = ListNode(val=int(val))
            res = res.next
        
        return res_head.next