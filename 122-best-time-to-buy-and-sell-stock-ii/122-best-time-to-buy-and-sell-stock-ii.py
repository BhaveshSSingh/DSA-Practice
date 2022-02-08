class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7,1,5,3,6,4
        # 5-1 =4
        # 3-6=3
        # max =7
        
        maxP = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                maxP += (prices[i+1]-prices[i])
        return maxP
          
        