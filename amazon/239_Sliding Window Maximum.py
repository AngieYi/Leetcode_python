'''
239. Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
For example,Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].
'''

'''
Keep indexes of good candidates in deque d.
The indexes in d are from the current window, they're increasing,
and their corresponding nums are decreasing.
Then the first deque element is the index of the largest window value.

For each index i:
Pop (from the end) indexes of smaller elements (they'll be useless).
Append the current index.

Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
If our window has reached size k, append the current window maximum to the output.
'''

import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 179ms 94.56%
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:   # compare current num with the last elements in the deque
                d.pop()                     # keep the largest elements in d[0]: any element less than n pop out
            d.append(i)                     # append the current index
            if d[0] == i - k:               # if the max is out of window
                d.popleft()                 # pop it from the front
            if i >= k - 1:                  # if window size already reach k, append max into output list
                out.append(nums[d[0]])
        return out

s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print s.maxSlidingWindow(nums,k)