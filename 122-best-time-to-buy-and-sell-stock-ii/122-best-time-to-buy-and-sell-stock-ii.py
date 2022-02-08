class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Loop through array 
        if the current number < next number 
        subtract
        and add all subtractions
        """
        sub = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                # print (prices[i],prices[i-1])
                sub += (prices[i] - prices[i-1])
        return sub
                
            