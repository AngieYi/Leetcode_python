'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
'''

class Solution(object):
    def climbStairs(self, n, cache={0:1, 1:1}):
        """
        :type n: int
        :rtype: int
        """

        '''
        if n in cache:
            return cache[n]
        cache[n] = self.climbStairs(n-1, cache) + self.climbStairs(n-2, cache)
        return cache[n]
        '''

        a,b = 1,1
        for _ in xrange(n-1):
            a,b = b, a+b
        return b