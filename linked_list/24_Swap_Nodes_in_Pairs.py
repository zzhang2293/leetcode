# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        dummy = ListNode(-1, next=head)
        '''
        dummy -> 1 -> 2 -> 3 -> 4
        '''
        pre = dummy.next
        cur = pre.next 
        dummy.next = cur
        while cur != None:
            #swap
            temp = cur.next 
            pre.next = temp 
            cur.next = pre 
            cur = temp.next 
        return dummy.next
    

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
obj = Solution()

res = obj.swapPairs(head=head)
print(res)
        
                       
        
        
        
