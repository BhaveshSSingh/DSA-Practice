class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mtn = prices[0]
        bp = 0
        
        for i in range(len(prices)):
            if bp < prices[i]-mtn:
                bp = prices[i]-mtn
            if mtn > prices[i]:
                mtn = prices[i]
        
        return bp