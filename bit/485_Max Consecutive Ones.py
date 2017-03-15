'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
             The maximum number of consecutive 1s is 3.
Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 85ms 83.03%
        n = 0
        maxn = 0
        for x in nums:
            if x == 1:
                n += 1
            else:
                maxn = max(maxn, n)
                n = 0
        maxn = max(maxn, n)
        return maxn

        '''
        # 3.75%
        str_num = ''.join(str(e) for e in nums)
        str_num = str_num.split('0')

        return max([len(s) for s in str_num])
        '''

s = Solution()
s.findMaxConsecutiveOnes([1,1,0,1,1,1])