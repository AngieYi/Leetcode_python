'''
153. Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 34ms 94.46%
        i = 0
        j = len(nums)-1
        while i < j:
            m = i + (j-i)/2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
        return nums[i]