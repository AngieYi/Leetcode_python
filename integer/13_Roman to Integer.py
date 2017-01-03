'''
13. Roman to Integer
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        Symbol	I	V	X	L	C	D	M
        Value	1	5	10	50	100	500	1,000

        Notation	IV	IX	XL	XC	CD	CM
        Number	    4	9	40	90	400	900
        '''

        '''
        # Note: if previous char is smaller than the later char, subtract it, otherwise add it
        # 148ms
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        int_sum = dic[s[-1]]

        for i in xrange(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                int_sum -= dic[s[i]]
            else:
                int_sum += dic[s[i]]

        return int_sum
        '''

        # 148ms
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        int_sum = 0

        if "IV" in s:
            s = s.replace("IV","")
            int_sum += 4
        if "IX" in s:
            s = s.replace("IX","")
            int_sum += 9
        if "XL" in s:
            s = s.replace("XL","")
            int_sum += 40
        if "XC" in s:
            s = s.replace("XC","")
            int_sum += 90
        if "CD" in s:
            s = s.replace("CD","")
            int_sum += 400
        if "CM" in s:
            s = s.replace("CM","")
            int_sum += 900

        for i in xrange(len(s)):
            int_sum += dic[s[i]]

        return int_sum