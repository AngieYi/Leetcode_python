'''
70. Climbing Stairs
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
        # DP,time: O(n); space: O(n)
        '''
        if n in cache:
            return cache[n]
        cache[n] = self.climbStairs(n-1, cache) + self.climbStairs(n-2, cache)
        return cache[n]
        '''

        # DP,time: O(n); space: O(1)
        a,b = 1,1
        for _ in xrange(n-1):
            a,b = b, a+b
        return b

    '''
    def fib_naive(n):   			# time:O(a^n)  1<a<2
      if n==1 or n==2:
        return 1
      return fib_naive(n-1) + fib_naive(n-2)

    def fib_memo1(n, cache = None):		# DP, time: O(n); space: O(n)
      if cache is None:
        cache = {}
      if n in cache:
        return cache[n]
      if n <= 2:
        cache[n] = 1
      else:
        fib_memo1(n-1, cache) + fib_memo1(n-2, cache)
      return cache[n]

    def fib_memo2(n, cache={0:1, 1:1}): 	# DP,time: O(n); space: O(n)
        if n in cache:
            return cache[n]
        cache[n] = fib_memo2(n-1, cache) + fib_memo2(n-2, cache)
        return cache[n]

    def fib_best(n): 			# DP,time: O(n); space: O(1)
        a, b = 1, 1
        for _ in xrange(n):
            a, b = b, a+b
        return b
    '''