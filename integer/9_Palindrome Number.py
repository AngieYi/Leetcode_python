'''
9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # 192ms 96.99%
        # extra space usually means O(n) extra space.
        # No extra space means O(1) extra space
        # 1. negative int and ten's multiples are not palindrome
        if x<0 or (x!=0 and x%10==0):
            return False

        # 2. reverse the second half until the second half >= first half
        rev = 0
        while x > rev:
            rev = rev*10 + x%10
            x = x/10

        # 3. even length(eg:1221): x==rev   odd length(eg:12 321): x==rev/10
        return x==rev or x==rev/10