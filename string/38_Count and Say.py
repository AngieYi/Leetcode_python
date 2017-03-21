'''
"Count and Say problem" Write a code to do following:
n String to print
0 1
1 1 1
2 2 1
3 1 2 1 1
...
Base case: n = 0 print "1"
for n = 1, look at previous string and write number of times a digit is seen and the digit itself.
In this case, digit 1 is seen 1 time in a row... so print "1 1"
for n = 2, digit 1 is seen two times in a row, so print "2 1"
for n = 3, digit 2 is seen 1 time and then digit 1 is seen 1 so print "1 2 1 1"
for n = 4 you will print "1 1 1 2 2 1"

Consider the numbers as integers for simplicity. e.g.
if previous string is "10 1" then the next will be "1 10 1 1" and the next one will be "1 1 1 10 2 1"
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'     # initially,n=0,string is "1"
        for _ in range(n-1):
            ref, temp, count = s[0], '', 0      # ref always be the first different char in a string
            for x in s:                         # s starts from "1", is changing depends on round
                if x == ref:                    # if x == ref, count +=1
                    count += 1
                else:
                    temp += str(count) + ref    # record the previous string
                    ref = x                     # prepare for next reference
                    count = 1                   # count reset to 1
            temp += str(count) + ref            # add the final string to temp
            s = temp                            # s reset to current temp, for next loop
        return s

p = Solution()
print p.countAndSay(4)