class Solution:
    def myPow(self, x: float, n: int) -> float:
        negativeX, negativeN = x<0 , n<0
        # abs are mods which turns -ve to +ve 
        x,n =abs(x) , abs(n)
        if n==0:
            return 1
        if n ==1:
            return 1/x if negativeN else x
        pwr = self.myPow(x , n//2)
        ans = pwr*pwr if n%2 == 0 else pwr*pwr*x
        
        if negativeX and n%2 ==1:
            ans = -ans
        if negativeN:
            ans = 1/ans
        
        return ans
         