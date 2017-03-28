'''
Write a function to find the longest common prefix string among an array of strings.
Input  : ["geeksforgeeks","geeks","geek","geezer"]
Output : "gee"

Input  : ["apple", "ape", "april"]
Output : "ap"
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 49ms 64.82%
        if not strs:
            return ""
        shortest = min(strs,key=len)        # pick the shortest str in the list
        for i, ch in enumerate(shortest):   # compare from the first element with str in the list
            for x in strs:
                if x[i] != ch:              # if there is difference
                    return shortest[:i]     # return shortest[0...i-1]
        return shortest                     # otherwise directly return shortest

        '''
        # 55ms 45.87%
        return os.path.commonprefix(strs)
        '''

s = Solution()
lis = ["apple", "ape", "april"]
print s.longestCommonPrefix(lis)