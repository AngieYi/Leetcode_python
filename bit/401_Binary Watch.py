'''
A binary watch has 4 LEDs on the top which represent the hours (0-11),
and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on,
return all possible times the watch could represent.

Example:
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid,
it should be "10:02".
'''

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for x in range(1024):
            if bin(x).count('1') == num:
                h, m = x >> 6, x & 0x3F
                if h < 12 and m < 60:
                    ans.append('%d:%02d' % (h, m))
        return ans


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        # 45 ms
        ans = []
        for x in range(1024):               # x = 0-1023, 10 lights are 10 bits, enumerate all possible 10 bits
            if bin(x).count('1') == num:
                h, m = x >> 6, x & 0x3F     # hour: 10 bits move right, left 4 bits;   minute: 0x3F = 0b111111
                if h < 12 and m < 60:
                    ans.append('%d:%02d' % (h, m))
        return ans

        '''
        # 48 ms
        ans = []
        for h in range(12):        # h: 0-11
            for m in range(60):    # m: 0-59
                if (bin(h)+ bin(m)).count('1') == num:  # bin(h): string, bin(h)+bin(m): string
                    ans.append('%d:%02d' % (h, m))      # %02d: two digits and may contain a leading zero
        return ans
        '''