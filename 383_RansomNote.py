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