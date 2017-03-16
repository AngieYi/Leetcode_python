'''
53. Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 65.98%
        if not nums:
            return 0

        curMax = finMax = nums[0]
        for x in nums[1:]:
            curMax = max(x, curMax + x)     # Current vs (curMax + Current)
            finMax = max(finMax, curMax)    # record the finMax

        return finMax