'''
342. Power of Four
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Example:
Given num = 16, return true. Given num = 5, return false.
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        '''
        # 46ms 72.4%
        if num <= 0:
            return False
        while num % 4 == 0:
            num = num / 4
        return True if num == 1 else False
        '''

        # 49ms 55.63%
        return num > 0 and num & (num-1) == 0 and num & 1431655765 == num

'''
        Consider the valid numbers within 32 bit, and turn them into binary form, they are:
                              1
                            100
                          10000
                        1000000
                      100000000
                    10000000000
                  1000000000000
                100000000000000
              10000000000000000
            1000000000000000000
          100000000000000000000
        10000000000000000000000
      1000000000000000000000000
    100000000000000000000000000
  10000000000000000000000000000
1000000000000000000000000000000

Any other number not it the list should be considered as invalid.
So if you XOR them altogether, you will get a mask value, which is:
1010101010101010101010101010101 (1431655765)
1. Any number <=0 is not power of 4.
2. Any number which is power of 4, it should be power of 2, use num &(num-1) == 0 to distinguish.(5:101 step3 not get rid of)
3. Check that if the number 'AND' the mask value is itself, to make sure it's in the list above.

final code:
return num > 0 and num &(num-1) == 0 and num & 1431655765== num

'''