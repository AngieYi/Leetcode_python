'''
520. Detect Capital
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        # 48ms 88.6%
        # istitle() only pass "Abc", "ABC","abc",other mixed title is not title.
        return word.isupper() or word.islower() or word.istitle()

        '''
        # 58 ms 51.74%
        if len(word) == 1:      # if only have one character,should be True
            return True

        if 'A' <= word[0] <= 'Z':                       # if first word is uppercase
            if 'a' <= word[1] <= 'z' and len(word)>=3:  # if second word is lowercase
                for x in word[2:]:                      # and rest of the word has uppercase, then False
                    if 'A' <= x <= 'Z':
                        return False
                return True
            elif 'A' <= word[1]<= 'Z' and len(word)>=3: # if second word is lowercase
                for x in word[2:]:                      # and rest of the word has uppercase, then False
                    if 'a' <= x <= 'z':
                        return False
                return True
            return True
        else:                   # if first word is lowercase
            for x in word[1:]:  # and rest of the word has uppercase, then False
                if 'A' <= x <= 'Z':
                    return False
        return True
        '''