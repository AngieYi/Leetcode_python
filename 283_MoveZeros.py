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