'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # 42 ms
        dic = {}
        for i,v in enumerate(nums): # enumerate costs O(n)
            if v in dic and i-dic[v] <= k:
                return True
            dic[v] = i
        return False

        '''
        # time exceed
        for i in xrange(len(nums)):
            if nums[i:].count(nums[i]) > 1:
                if i+1 < len(nums):
                    j = nums[i+1:].index(nums[i])+ i+1
                    if abs(i-j) <= k:
                        return True
        return False
        '''

