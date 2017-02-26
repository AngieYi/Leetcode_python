'''
Given an integer, write a function to determine if it is a power of two.
'''

class Solution(object):
      def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
         '''
        # 52ms
        return n > 0 and not (n & n-1)
        '''

        # 42ms,91.98%
        if n <= 0:
            return False
        while n%2 == 0:
            n = n / 2
        return True if n == 1 else False

s = Solution()
print s.isPowerOfTwo(9)