'''
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
'''

'''
The basic idea is that we set two pointers l and r to the left and right end of height.
Then we get the minimum height (minHeight) of these pointers (similar to Container with Most Water
due to the Leaking Bucket Effect) since the level of the water cannot be higher than it.
Then we move the two pointers towards the center.
If the coming level is less than minHeight, then it will hold some water.
Fill the water until we meet some "barrier" (with height larger than minHeight)
and update l and r to repeat this process in a new interval.
'''

class Solution:
    """
    :type height: List[int]
    :rtype: int
    """
    def trap(self, height):
        l, r, water, minHeight = 0, len(height) - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while l < r and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water

ob = Solution()
#print ob.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print ob.trap([1,0,2,1])