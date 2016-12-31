'''
168. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''

import math

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """


        '''
        A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
        B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
        .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
        .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
        .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
        Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
        '''



        # 39 ms
        # recursively set the charaters from right to left
        if n == 0:
            return ""
        else:
            return self.convertToTitle((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))


        '''
        # not work
        # recursively set the charaters from left to right
        if n <= 0: return ""

        x = int(math.log(n,26))
        y = n / pow(26,x)

        if n == y * pow(26,x):
            return self.convertToTitle((n-1) / 26) + "Z"   # end with "Z"
        else:
            return chr(y -1 + ord("A")) + self.convertToTitle(n - y * pow(26,x))
        '''


        '''
        # 45ms
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while n > 0:
            result.append(capitals[(n-1)%26])
            n = (n-1) // 26
        result.reverse()
        return ''.join(result)
        '''