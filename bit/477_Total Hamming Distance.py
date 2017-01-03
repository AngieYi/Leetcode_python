'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
'''

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        Total hamming distance is the sum of the hamming distance for each of the i-th bits separately.
        The total hamming distance would be the number of pairs of numbers that are different. That is,
        Total hamming distance for the i-th bit =
        (number of 0 in i-th position) * (the number of 1 in i-th position).
        then sum together to get our answer.
        >>> x = [1, 2, 3]
        >>> y = [4, 5, 6]
        >>> zip(x, y)
        [(1, 4), (2, 5), (3, 6)]

        >>> map('{:032b}'.format,nums)
['00000000000000000000000000000100', '00000000000000000000000000001110', '00000000000000000000000000000010']

        >>> zip(['0100','1110','0010'])
        >>> [('0100',), ('1110',), ('0010',)]

        >>> zip(*['0100','1110','0010'])
        >>> [('0', '1', '0'), ('1', '1', '0'), ('0', '1', '1'), ('0', '0', '0')]

        '''

        '''
        # 295ms: shortest line
        return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))
        '''

        # 292ms: more readable
        bsum = 0
        for tuple_bit in zip(*map('{:032b}'.format,nums)):
            bsum += tuple_bit.count('0') * tuple_bit.count('1')
        return bsum



        '''
        # Time exceed,brute force
        bsum = 0
        for i in xrange(len(nums)-1):
            for j in xrange(i+1,len(nums)):
                bsum += bin(nums[i]^nums[j]).count("1")
        return bsum
        '''