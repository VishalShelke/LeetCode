#Sliding Window: Best Time to Buy and Sell Stock - Leetcode 121

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # two poitners
        # l = left pointer, r = right pointer
        l ,r = 0,1
        #max profir
        maxP= 0

        while r<len(prices):
            if prices[r]-prices[l]>0:# if the price at right pointer is greater than the left pointer
                # update the max profit                
                maxP=max(maxP,prices[r]-prices[l])
            else:
                # if the price at right pointer is less than the left pointer
                # move the left pointer to the right
                l=r
            r+=1

        return maxP