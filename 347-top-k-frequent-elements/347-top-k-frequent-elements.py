class Solution(object):
    def topKFrequent(self, nums, k):
        freq,hp = Counter(nums),[]
        for el,count in freq.items():
            heapq.heappush(hp,(count,el))
            if len(hp)>k:
                heapq.heappop(hp)
        return [x[1]for x in hp]