# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head = p = ListNode(0,head)
        l=r=head.next
        while r:
            # if value equal (or on the same node)
            if r.val == l.val:
                r= r.next
                # agar r ek kadam dhur hai kya
            elif l.next is r:
                p.next = l
                p = p.next
                l = r
                # jumping to other nodes
            else:
                l = r
        # if the LL is finished or return L        
        p.next= None if l.next else l
        return head.next