'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times)
with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:
prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 42ms 95.34%
        if len(prices) < 2:
            return 0
        buy, ans, pbuy, psell = -prices[0], 0, 0, 0
        for x in prices:
            pbuy = buy
            buy = max(psell - x, pbuy)
            psell = ans
            ans = max(pbuy + x, psell)
        return ans


        '''
        # 62ms 27.46%
        # free is the max profit I can have while being free to buy.
        # have is the max profit I can have while having stock.
        # cool is the max profit I can have while cooling down.
        free = 0
        have = cool = float('-inf')
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
        return max(free, cool)
        '''

s = Solution()
prices = [1, 2, 3, 0, 2]
s.maxProfit(prices)