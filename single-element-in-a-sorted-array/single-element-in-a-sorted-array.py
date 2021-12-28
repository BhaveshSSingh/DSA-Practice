class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        
        # boundary checks
        if h == 0:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[h] != nums[h-1]:
            return nums[h]
    
    # binary search
        while l<=h:
            m = (l+h)//2
            if nums[m] != nums[m-1] and nums[m] != nums [m+1]:
                return nums[m]
            if (m%2==0 and nums[m] == nums[m+1]) or (m%2 !=0 and nums[m] == nums[m-1]):
                l = m+1
            else:
                h = m -1
        return -1
