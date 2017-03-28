'''
Given a range [m, n] where 0 <= m <= n <= 2147483647,
return the bitwise AND of all numbers in this range, inclusive.
For example, given the range [5, 7], you should return 4.
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        # 56.11%
        if m == n:
            return m
        zeros = len(bin(m^n)) - 2         # find highest diff bit position (XOR is 1),lowers are all zeros after AND,-2(ignore '0b')
        return (n >> zeros) * (2**zeros)  # (get all high identical bit) * (all zero bit)

s = Solution()
print s.rangeBitwiseAnd(6,8)