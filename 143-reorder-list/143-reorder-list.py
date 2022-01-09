def cutInHalf(head):
    fast , slow =  head.next ,head
    # if only 1 node
    if not fast:
        return None
    # if more than 1 node
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    if fast.next:
        slow = slow.next
    x = slow.next
    slow.next = None
    return x

def reverse(head):
    if not head or not head.next:
        return head
    p,c,n = head , head.next, head.next.next
    p.next = None
    while n:
        c.next = p
        p,c,n = c,n,n.next
    c.next = p
    return c
    
    
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        h = cutInHalf(head)
        h = reverse(h)
        p = head
        while p and h:
            h2= h.next
            h.next= p.next
            p.next = h
            p , h = p.next.next, h2
        return head
        