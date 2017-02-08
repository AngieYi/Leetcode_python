'''
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

from collections import Counter
import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 49ms
        return sorted(nums)[len(nums)/2]

        '''
        # 52ms
        mini = len(nums)/2
        for x in set(nums):             # list convert to set, time complexity is O(n)
            if nums.count(x) > mini:
               return x
        '''


        '''
        # 58ms
        final = []
        mini = len(nums)/2
        for x in set(nums):
            if nums.count(x) > mini:
                final.append(x)
        if len(final) == 1:
            return final[0]
        else:
            return final
        '''

        '''
        # 85 ms
        final = []
        tmp = Counter(nums).items()
        mini = len(nums)/2
        for x,cnt in tmp:
            if cnt > mini:
                final.append(x)
        if len(final) == 1:
            return final[0]
        else:
            return final
        '''

        '''
        # 92 ms
        return Counter(nums).most_common(1)[0][0]
        '''

        '''
        About collections.Counter, dict, defaultdict

        You can use Counter like this

        from collections import Counter
        alist=[1,1,1,2,2,3,4,2,2,3,2,2,1]
        print Counter(alist)
        If you want to use your solution, you can improve it like this

        def icount(alist):
            adic = {}
            for i in alist:
                adic[i] = adic.get(i, 0) + 1
            return adic
        Even better, you can use defaultdict like this

        from collections import defaultdict
        adic = defaultdict(int)
        for i in alist:
            adic[i] += 1
        return adic

       '''