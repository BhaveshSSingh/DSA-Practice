class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = dict()
        
        for i,x in enumerate(nums):
            if target-x in m:
                return[m[target-x],i]
            m[x] = i