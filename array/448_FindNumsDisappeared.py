'''
448. Find All Numbers Disappeared in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

similar to 442
'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        # without extra space, O(n)335ms
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in xrange(len(nums)) if nums[i] > 0]


        '''
        # use set 242ms
        return set(range(1,len(nums)+1)) - set(nums)
        '''

        '''
        # use filter: run out of time
        li_num = []
        for i in xrange(1,len(nums)+1):
            li_num.append(i)
        return filter(lambda x: x not in nums,li_num)
        '''

        '''
        # use dictionary 254ms
        dic = {}
        li_disappear = []
        for x in nums:
            dic[x] = dic.get(x,0)+1

        for i in xrange(1,len(nums)+1):
            if dic.get(i,0) == 0:
                li_disappear.append(i)
        return li_disappear
        '''

        '''
        difference between range and xrange
        range(): range(1, 10) returns a list from 1 to 10 numbers & hold whole list in memory.
        xrange(): Like range(), but instead of returning a list, returns an object that generates the numbers in the range on demand. For looping, this is lightly faster than range() and more memory efficient. xrange() object like an iterator and generates the numbers on demand.(Lazy Evaluation)
        In [1]: range(1,10)
        Out[1]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
        In [2]: xrange(10)
        Out[2]: xrange(10)
        In [3]: print xrange.__doc__
        xrange([start,] stop[, step]) -> xrange object
        '''