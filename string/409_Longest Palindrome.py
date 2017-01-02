'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 48ms
        length = 0
        tag = False
        for x in xrange(ord("A"),ord("z")+1):
            if s.count(chr(x))%2 == 0:      # count = 0 or even
                length += s.count(chr(x))
            else:
                length += s.count(chr(x))-1
                tag = True
        return length+1 if tag else length