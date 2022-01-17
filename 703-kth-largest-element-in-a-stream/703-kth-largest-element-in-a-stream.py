class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp=[]
        self.k = k
        for el in nums:
            if len(self.hp)<k or self.hp[0]<el:
                heapq.heappush(self.hp,el)
            if len(self.hp)>k:
                heapq.heappop(self.hp)

    def add(self, val: int) -> int:
        if len(self.hp)<self.k or self.hp[0]<val:
            heapq.heappush(self.hp,val)
        if len(self.hp)>self.k:
            heapq.heappop(self.hp)
        return self.hp[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)