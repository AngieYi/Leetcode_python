'''
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 45 ms 52.07%
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []



        '''
        Consider this case where the s = {{{}}}
        Replace function will replace only one set {} at a time.
        Replace itself takes O(N) time because it will have to search the entire string.
        On top of this, we have while loop which runs for O(N/2) times.
        So O(N) * O(N/2) results in O(N^2)
        '''

        '''
        # 129 ms
        # too too slow
        # O(n^2)
        n = len(s)
        if n == 0:
            return True

        if n % 2 != 0:
            return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')

        if s == '':
            return True
        else:
            return False

        '''