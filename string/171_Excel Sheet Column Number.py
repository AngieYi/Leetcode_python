'''
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''
# related to 168
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 48 ms
        sum = 0
        for i in xrange(len(s)):
            sum += (ord(s[i]) - ord("A") + 1) * pow(26,(len(s)-i-1))
        return sum

        #return (len(s) - 1) * 26 + ord(s[-1]) - ord("A") + 1 # could not pass "BA"