import heapq 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for el in nums:
            if len(hp)< k or hp[0]<el:
                heapq.heappush(hp,el)
            if len(hp) > k:
                heapq.heappop(hp)
#                 hp[0] = top of min heap
        return hp[0]