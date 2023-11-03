class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(next=head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            group_next = kth.next 
            prev, curr = kth.next , groupPrev.next
            while curr != group_next:
                tmp = curr.next 
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
    def getKth(self, curr, k) -> ListNode:
        while curr and k > 0:
            k -= 1
        return curr
            
        
            
node = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
obj = Solution()
obj.reverseKGroup(node, 2)
