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
        target = head
        detect = head
        dummy = ListNode(None, next=head)
        pre = dummy
        for i in range(n):
            detect = detect.next 
        while detect:
            detect = detect.next 
            target = target.next 
            pre = pre.next
        pre.next = target.next 
        return dummy.next
            