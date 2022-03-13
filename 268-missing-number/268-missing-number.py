class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ans =  len(nums) - 1
        # print len(nums)
        # return ans
        
        # res = len(nums)
        # # print(res)
        # for i in range(len(nums)):
        #     res += (i - nums[i])
        #     print res
        # return res
        
        ans =sum(range(len(nums)+1)) - sum(nums) 
        # print (range(len(nums)+1))
        return ans