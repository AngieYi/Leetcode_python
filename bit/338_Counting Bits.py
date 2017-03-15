'''
Given a non negative integer number num.
For every numbers i in the range between 0 and num,
calculate the number of 1's in their binary representation and return them as an array.

Example: For num = 5 you should return [0,1,1,2,1,2].

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?

Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount
in c++ or in any other language.

Hint:
You should make use of what you have produced already.
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on.
And try to generate new range from previous.
Or does the odd/even status of the number help you in calculating the number of 1s?
'''

class Solution(object):
    # 88.16%
    def countBits(self, num):
        ans=[0]
        while len(ans) <= num:
            ans += [i+1 for i in ans]
        return ans[:num+1]

    '''
    # 235ms 42.19%
        ans = []
        for x in xrange(num+1):
            ans.append(bin(x)[2:].count("1"))
        return ans
    '''

s = Solution()
print s.countBits(5)