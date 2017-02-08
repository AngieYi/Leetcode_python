'''
387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''
import string

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """


        # 75 ms
        L = []
        for c in string.ascii_lowercase:
            if s.count(c) == 1:         # s.count costs O(n)
                L.append(s.find(c))     # s.find costs O(n)

        if len(L) >= 1:
            return min(L)
        else:
            return -1


        '''
        # 99ms
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
        '''


        '''
        # time exceed: go through each element until one meet requirement
        for i in xrange(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
        '''

        '''
        # wrong: set change the original string order
        S = set(s)
        for x in S:
            if s.count(x) == 1:
                return s.index(x)
        return -1
        '''

        '''
        Difference between find and index?
        str.find returns -1 when it does not find the substring.

        >>> line = 'hi, this is ABC oh my god!!'
        >>> line.find('?')
        -1

        While str.index raises ValueError:
        >>> line.index('?')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        ValueError: substring not found
        '''