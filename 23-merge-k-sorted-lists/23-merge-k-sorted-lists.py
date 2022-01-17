
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap,(head.val,head))
        ans = ListNode()
        pointer = ans
        while len(heap) > 0:
            n = heapq.heappop(heap)[1]
            pointer.next = n
            pointer = n
            if n.next:
                heapq.heappush(heap,(n.next.val,n.next))
        return ans.next
        