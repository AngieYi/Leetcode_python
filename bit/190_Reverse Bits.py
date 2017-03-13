'''
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).
'''

class Solution:
    # @param n, an integer
    # @return an integer

    def reverseBits(self, n):
        # 46ms,76.46%
        ans = 0
        for i in xrange(32):
            ans = ans << 1  # turn left handover the lowest bit position
            ans += n & 1    # get the lowest bit
            n >>= 1         # turn right ignore the rightest bit
        return ans

        '''
        # 55ms, 31.78%
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)
        '''

        '''
        # 49ms, 54.79%
        rebitn = ""
        bitn = bin(n)[2:]               # get bit of n,ignore first two charater "0b"
        for i in xrange(1,len(bitn)+1): # use negative index of bitn string
            rebitn += bitn[(-1)*i]      # append to a new string to generate a reversed bitn
        rebitn = rebitn + "0"*(32-len(rebitn))  # add "0" after it.
        return int("0b"+rebitn,2)       # change bit into integer
        '''

n = 43261596
s = Solution()
print s.reverseBits(n)