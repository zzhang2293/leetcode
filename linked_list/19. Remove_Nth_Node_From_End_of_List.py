# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        '''
            1 2 3 4 5
        '''
        
        dummy = pre = ListNode(next=head)
        fast:ListNode = head
        slow = head
        for i in range(n - 1):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next 
            pre = pre.next
        
        pre.next = slow.next 
        return dummy.next