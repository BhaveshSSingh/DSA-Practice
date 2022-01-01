class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if nums[0] < nums[-1]: return nums[0]
        front = 0
        last = len(nums)-1
        while front <= last:
            mid = (front + last )//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid -1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[front]:
                front = mid+1
            else:
                last = mid-1