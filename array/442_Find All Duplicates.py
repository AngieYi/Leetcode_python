'''
442. Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

similar: 448
'''

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 305ms
        dic = {}
        li_dup = []

        for x in nums:
            dic[x] = dic.get(x,0) + 1

        for x in nums:
            if dic[x] == 2:
                li_dup.append(x)
                dic[x] = -1

        return li_dup


        '''
        # 315ms
        li_dup = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                li_dup.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return li_dup
        '''