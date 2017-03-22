'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, k between [1,number of unique elements].
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        x = []
        print collections.Counter(nums)
        for item in collections.Counter(nums).most_common(k):
            x.append(item[0])
        return x

nums = [1,1,1,2,2,3]
k = 2
s = Solution()
s.topKFrequent(nums,k)