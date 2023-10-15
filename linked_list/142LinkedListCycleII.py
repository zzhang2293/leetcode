#https://leetcode.cn/problems/linked-list-cycle-ii/description/
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position
# (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the
# linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        1. 快慢指针，如果有环，快指针一定会追上慢指针
        2. 从头开始走，快慢指针一定会在环的入口处相遇
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next 
                return slow
        return None
