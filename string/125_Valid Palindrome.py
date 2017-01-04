'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 79ms 70%
        # two pointer inplace
        L,R = 0,len(s)-1
        while L<R:
            while L<R and not s[L].isalnum():
                L += 1
            while L<R and not s[R].isalnum():
                R -= 1
            if s[L].upper() != s[R].upper():
                return False
            L += 1
            R -= 1
        return True  # all handled such as empty str or without isalnumone


        '''
        # Time Limit Exceeded
        if len(s) == 0: # empty string is palindrome
            return True

        seq = ""
        rev = ""
        for x in s:
            if 48<=ord(x)<= 57 or 65<=ord(x)<=90: # numeric and upper case
                seq += x
                rev = x+rev
            elif 97<=ord(x)<=122:               # lower case
                seq += x.upper()
                rev = x.upper()+rev

        return seq == rev
        '''