'''
12. Integer to Roman
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''
from collections import OrderedDict
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        '''
        Symbol	I	V	X	L	C	D	M
        Value	1	5	10	50	100	500	1,000

        Notation	IV	IX	XL	XC	CD	CM
        Number	    4	9	40	90	400	900
        '''

        '''
        # 339ms
        dic = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",
               50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        dic = OrderedDict(sorted(dic.items(),reverse= True))
        '''

        '''
        # 325ms
        dic = OrderedDict([(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),
                           (50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")])
        '''


        # 115ms
        l_tup = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),
                 (50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

        final = ""
        for k,v in l_tup:
            if num > 0:
                final += num/k * v
                num = num%k
        return final


        '''
        # 175ms
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]
        '''


        '''
        OrderedDict VS Dict

       An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.

        import collections

        print 'Regular dictionary:'
        d = {}
        d['a'] = 'A'
        d['b'] = 'B'
        d['c'] = 'C'
        d['d'] = 'D'
        d['e'] = 'E'

        for k, v in d.items():
            print k, v

        print '\nOrderedDict:'
        d = collections.OrderedDict()
        d['a'] = 'A'
        d['b'] = 'B'
        d['c'] = 'C'
        d['d'] = 'D'
        d['e'] = 'E'

        for k, v in d.items():
            print k, v

        A regular dict does not track the insertion order, and iterating over it produces the values in an arbitrary order. In an OrderedDict, by contrast, the order the items are inserted is remembered and used when creating an iterator.

        $ python collections_ordereddict_iter.py

        Regular dictionary:
        a A
        c C
        b B
        e E
        d D

        OrderedDict:
        a A
        b B
        c C
        d D
        e E


        --------------------------------------------
        Equality

        A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.

        import collections

        print 'dict       :',
        d1 = {}
        d1['a'] = 'A'
        d1['b'] = 'B'
        d1['c'] = 'C'
        d1['d'] = 'D'
        d1['e'] = 'E'

        d2 = {}
        d2['e'] = 'E'
        d2['d'] = 'D'
        d2['c'] = 'C'
        d2['b'] = 'B'
        d2['a'] = 'A'

        print d1 == d2

        print 'OrderedDict:',

        d1 = collections.OrderedDict()
        d1['a'] = 'A'
        d1['b'] = 'B'
        d1['c'] = 'C'
        d1['d'] = 'D'
        d1['e'] = 'E'

        d2 = collections.OrderedDict()
        d2['e'] = 'E'
        d2['d'] = 'D'
        d2['c'] = 'C'
        d2['b'] = 'B'
        d2['a'] = 'A'

        print d1 == d2
        In this case, since the two ordered dictionaries are created from values in a different order, they are considered to be different.

        $ python collections_ordereddict_equality.py

        dict       : True
        OrderedDict: False
       '''


