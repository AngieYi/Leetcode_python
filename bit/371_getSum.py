'''
371. Sum of Two Integers
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
Example:
Given a = 1 and b = 2, return 3.
'''

def getSum(self, a, b):
    MAX_INT = 0x7FFFFFFF
    MIN_INT = 0x80000000
    MASK = 0x100000000
    while b:
        a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

'''
What's hexadecimal ?
As each hexadecimal digit represents four binary digits (bits),
it allows a human-friendly representation of binary-coded values.
For example, a single byte can have values ranging from 00000000 to 11111111,
in binary, but this is more conveniently represented as 00 to FF in hexadecimal.

Python: long and int ?
in my machine cywin:
>>> print type(0x7FFFFFFFFFFFFFFF)
<type 'int'>

>>> print type(0x7FFFFFFFFFFFFFFF + 1)
<type 'long'>


python return if else?
These three versions are the same.
1)
if(A > B):
    return A+1
return A-1

2)
if(A > B):
    return A+1
else:
    return A-1

3)return A+1 if A > B else A-1

'''

'''
Python整数不是固定的32位，所以需要做一些特殊的处理，
代码里的将一个数对0x100000000取模（注意：Python的取模运算结果恒为非负数），
是希望该数的二进制表示从第32位开始到更高的位都同是0（最低位是第0位），以在0-31位上模拟一个32位的int。

python因为自动整数越界为long。用python要用0x10000000 (33位）做mask取模保持int。
'''

'''
32位的int，正数的范围是(0,0x7FFFFFFF),负数(0x80000000,0xFFFFFFFF)
'''


'''
# First iteration (a is 20, b is 20)
10100 ^ 10100 == 00000              # makes a 0
(10100 & 10100) << 1 == 101000      # makes b 40

# Second iteration:
000000 ^ 101000 == 101000           # Makes a 40
(000000 & 101000) << 1 == 0000000   # Makes b 0


What do the masks do?
All the masks ensures that the value is an integer.
Since the maximum possible int (32 bits) is 2147483647, if you add 2 to this value,
like you did in your example,the int overflows and you get a negative value.
You have to force this in Python, because it doesn't respect this int boundary as strongly
typed languages like Java and C++ have defined.

Consider the following:
def get_sum(a, b):
    while b:
        a, b = (a ^ b), (a & b) << 1   # without the masks
    return a

print get_sum(2147483647, 2)
outputs: 2147483649

while
print Solution().getSum(2147483647, 2)
outputs: -2147483647

due to the overflow.
'''

'''
Python has more than 32 bits for integers. You can try to run "print 2 ** 31"
Python would shows the exact number correctly,
while other languages like Java would not. Java only recognizes -2 ** 31 to 2 ** 31 - 1.

How does integers presented in Python differ from integers in 32-bit e.g. Java?
From what I heard, Python has 64 bits. (Please let me know if I am wrong. )
So 1 in Python would look like 0x0000000000000001, but it looks like 0x00000001 in 32-bit format.
-1 in Python would look like 0xFFFFFFFFFFFFFFFF, but it looks like 0xFFFFFFFF in 32-bit format.

It seems that the input given by LC is in 32-bit format.
Since Python would treat it as positive with 1 on the 32 position,
we have to use mask to treat it as negative.
'''