#https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA:ListNode, headB:ListNode):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        根据快慢法则，走的快的一定会追上走得慢的。
        在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

        那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
        位置相遇
        """
        cur_a, cur_b = headA, headB     # 用两个指针代替a和b

        
        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB      # 如果a走完了，那么就切换到b走
            cur_b = cur_b.next if cur_b else headA      # 同理，b走完了就切换到a
        
        return cur_a
        