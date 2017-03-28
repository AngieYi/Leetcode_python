'''
You are given two arrays without duplicates nums1 and nums2 where nums1 elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
For number 2 in the first array, the next greater number for it in the second array is 3.
For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
'''

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # 55ms, 90+%
        d = {}      # dict key is element,value is the next bigger element
        stk = []    # stack save all the element into it
        ans = []    # array save answer

        for x in nums:
            while len(stk) and stk[-1] < x:   # As long as there's num in stack less than x
                d[stk.pop()] = x              # {num:x} will be record in dict
            stk.append(x)                     # save x into stack

        for y in findNums:
            ans.append(d.get(y, -1))          # if in dict,get value, otherwise get -1

        return ans

        '''
        # 99ms, 52.37%
        ans = []
        for i in xrange(len(findNums)):
            j = nums.index(findNums[i])
            if j == len(nums)-1:                # already last element
                ans.append(-1)
            else:
                for t in xrange(j+1,len(nums)):
                    if nums[t] > findNums[i]:   # if exists bigger, append element then break
                        ans.append(nums[t])
                        break
                    if t == len(nums)-1:        # if not break and loop until the end,append -1
                        ans.append(-1)
        return ans
       '''



# findNums = [3,1,5,7,9,2,6]
# nums = [1,2,3,5,6,7,9,11]

findNums = [3,1,2]
nums = [1,3,2,4]
s = Solution()
print s.nextGreaterElement(findNums,nums)