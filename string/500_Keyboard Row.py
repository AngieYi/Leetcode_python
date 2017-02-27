'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's
of American keyboard like the image below.
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        # use set
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        answer = []
        for w in words:
            x = set(w.lower())

            # 39ms, 77.06%
            if x<=a or x<=b or x<=c:
                answer.append(w)

            # 42ms 59.3%
            # if not x-a or not x-b or not x-c:
            #     answer.append(w)

            # 55ms 20.5%
            # if a&x == x:
            #     answer.append(w)
            # elif b&x == x:
            #     answer.append(w)
            # elif c&x == x:
            #     answer.append(w)

        return answer



        # using regular expression
        '''
        # 49ms 32.77%
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)

        # 32.77%
        pattern = "^[qwertyuiop]*$|[asdfghjkl]*$|[zxcvbnm]*$"
        ans = []
        for w in words:
            if re.match(pattern, w, re.I):
                ans.append(w)
        return ans
        '''