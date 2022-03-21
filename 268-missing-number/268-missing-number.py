class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = sum(range(len(nums)+1)) - sum(nums)
        return ans