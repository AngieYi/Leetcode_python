'''
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
The input is assumed to be a 32-bit signed integer.
Your function should return 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 59ms 58.3%
        digits = []

        if x==0:
            return 0

        remains = abs(x)
        sign = -1 if x < 0 else 1

        while True:
            digit = remains % 10
            remains = remains / 10
            digits.append(digit)
            if remains == 0:
                break

        ans = 0
        for i in digits:
            ans *= 10
            ans += i

        ans *= sign
        if abs(ans) > 0x7FFFFFFF:
            return 0
        else:
            return ans

        '''
        # 71.09%
        s=cmp(x,0);r=int(`s*x`[::-1]);return (r<2**31)*s*r
        '''

s = Solution()
s.reverse(321)