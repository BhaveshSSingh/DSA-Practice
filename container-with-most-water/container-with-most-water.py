class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        l = 0
        r =len(height) -1
        while l<r :
            hL , hR = height[l],height[r]
            maxWater =  max(maxWater , min(hL, hR)* (r-l))
            if hL>= hR :
                r -=1
            if hL<= hR:
                l +=1
        return maxWater
        
        