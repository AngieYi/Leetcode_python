'''
Implement int sqrt(int x).
Compute and return the square root of x.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        # 69.52%
        L, R = 0, x
        while L <= R:
            mid = L + (R-L)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                R = mid
            else:
                L = mid + 1
        '''

        # 69.52%
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r