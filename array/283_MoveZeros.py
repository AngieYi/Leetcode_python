'''
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # 59ms
        L = len(nums)
        p = 0
        for i in xrange(L):
            if nums[i] != 0:
                nums[i],nums[p] = nums[p],nums[i]
                p += 1

        # 282ms
        for x in nums:
            if x == 0:
                nums.remove(x)
                nums.append(0)