class NumArray:

    def __init__(self, nums: List[int]):
        self.runningTotal = [0]
        for num in nums:
            self.runningTotal += self.runningTotal[-1] +num,
        

    def sumRange(self,i,j) -> int:
        return self.runningTotal[j+1] - self.runningTotal[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)