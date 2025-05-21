#Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #maxsum initialized to the first element
        #cursum initialized to 0
        maxsum=nums[0]
        cursum=0

        for i in nums:
            # if cursum is less than 0, set it to 0
            if cursum<0:
                cursum=0
            cursum+=i
            maxsum=max(maxsum, cursum)
        return maxsum