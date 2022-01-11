# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        curr = head
        
        while curr:
            prev = dummyHead
            nex = dummyHead.next 
            while nex:
                if curr.val < nex.val:
                    break
                prev = prev.next
                nex = nex.next
            temp = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = temp 
    
        return dummyHead.next