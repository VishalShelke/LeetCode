# 238. Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1]*(len(nums))
        # prefix product
        prefix=1
        for i in range(len(nums)):
            # prefix product of all elements before index i    
            res[i]=prefix
            prefix *=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res