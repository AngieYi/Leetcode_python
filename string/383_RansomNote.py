'''
383. Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        """
        str.count(sub, start= 0,end=len(string))
        list.count(obj)

        """


        # 69ms, beat > 90%
        s = set(ransomNote)
        for x in s:
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True


        '''
        # 182ms
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
        '''

        '''
        # time limit exceeds
        L = list(magazine)
        for x in ransomNote:
            if L.count(x):
                L.remove(x)
            else:
                return False
        return True
        '''

        # could not pass
        # Input: "aa", "ab"
        # Output: ture
        # expected: false

        '''
        if (set(ransomNote) - set(magazine)) == set([]):
            return True
        else:
            return False
        '''

        # could not pass
        # Input: "fffbfg", "effjfggbffjdgbjjhhdegh"
        # Output: false
        # Expected: true

        '''
        if magazine.count(ransomNote)==0:
            return False
        else:
            return True
        '''