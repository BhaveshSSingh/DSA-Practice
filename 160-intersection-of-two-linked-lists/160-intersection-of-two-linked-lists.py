# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        m = {}
        p = headA
        while p:
            m[id(p)] = p
            p = p.next
        p = headB
        while p:
            if id(p) in m:
                return p
            p = p.next
        return None