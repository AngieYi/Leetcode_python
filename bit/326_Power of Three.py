'''
Given an integer, write a function to determine if it is a power of three.
Follow up:
Could you do it without using any loop / recursion?
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        # 225ms,44.52%
        if n <= 0:
            return False

        while n%3 == 0:
            n = n / 3

        return n == 1
        '''

        # 248ms,21.55%
        return n > 0 and 1162261467 % n == 0 # maximum integer of pow 3 in python 2.7.