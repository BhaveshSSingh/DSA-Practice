class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = max(nums)
        # edge case => the  list given is all negative
        if maxNum < 0 :
            return maxNum
        
        maxSum = 0
        currSum = 0 
        
        for num in nums:
            currSum += num
            
            if maxSum < currSum:
                maxSum = currSum
            
            if currSum < 0:
                currSum = 0
        
        return maxSum
            