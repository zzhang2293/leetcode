class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_lst_dummy = ListNode()
        res_lst = res_lst_dummy
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    res_lst.next = ListNode(val=list1.val)
                    list1 = list1.next
                else:
                    res_lst.next = ListNode(val=list2.val)
                    list2 = list2.next
            elif list1:
                res_lst.next = ListNode(val=list1.val)
                list1 = list1.next
            elif list2:
                res_lst.next = ListNode(val=list2.val)
                list2 = list2.next
            res_lst = res_lst.next
        return res_lst_dummy.next
            
                    