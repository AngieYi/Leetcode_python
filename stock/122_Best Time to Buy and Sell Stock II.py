'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 55ms 45.89%
        # if tomorrow's price is higher than today's, we buy it today and sell tomorrow. Otherwise, we don't.
        '''
         1. you cannot hold more than one transaction at any time, this solution does not contradict with this.
            I am selling everything before buying anything.
         2. Just in case you haven't noticed, this kind of transaction (selling and buying on the same day) is redundant.e.g. if you buy on day 1, sell on day 2, buy on day 2 and sell on day 3, the profit is exactly the same as buying on day 1 and selling on day 3.
        '''
        ans = 0
        for i in xrange(len(prices)-1):
            if prices[i+1] > prices[i]:
                ans += prices[i+1]-prices[i]
        return ans