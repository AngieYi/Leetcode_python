def reverseString0(s):
        L = len(s)
        a = ""
        for i in xrange(1,L+1):
            a += s[-i]
        return a

from collections import deque
def reverseString(s):
        L = len(s)
        a = deque()
        for i in xrange(L):
            a.appendleft(s[i])
        return ''.join(a)


print reverseString("abc defg")