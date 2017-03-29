'''
438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]

Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]

'''

from collections import Counter
from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

 		# 165ms 96.51%
        # Time complexity can be reduced down to O(len(s)) if you use a dictionary instead of a Counter.
        # Same idea, just keep a sliding window and delete the keys when they reach zero.
        # There's no need for Counter comparison (which is O(len(p)), since you can just check if the dictionary is empty.

        d = defaultdict(int)
    	ns, np = len(s), len(p)
    	ans = []

    	for c in p:	d[c] -= 1  # default num of every char in p is -1

    	for i in xrange(ns):  # loop s
    		if i < np:
    			d[s[i]] += 1  # if char also in s, num of the char will be 0
    			if not d[s[i]]: del d[s[i]]   # delete this char
    		else:
    			if not d: ans.append(i-np)    # if d is empty,then this substring is valid

    			d[s[i-np]] -= 1
    			if not d[s[i-np]] : del d[s[i-np]]

    			d[s[i]] += 1
    			if not d[s[i]]: del d[s[i]]

    	if not d: ans.append(i-np+1)

    	return ans


        '''
        # 195ms 82.48%
        res = []
        ns, np = len(s), len(p)

        if ns < np: return res

        phash, shash = [0]*123, [0]*123

        for x in p:
            phash[ord(x)] += 1

        for x in s[:np-1]:
            shash[ord(x)] += 1

        for i in range(np-1, ns):
            shash[ord(s[i])] += 1
            if i-np >= 0:
                shash[ord(s[i-np])] -= 1
            if shash == phash:
                res.append(i - np + 1)

        return res
        '''

        '''
        # did not work
        d = defaultdict(int)
        L = []
        for i in xrange(0,len(s)-len(p)+1):
            sub = s[i:i+len(p)]
            for x in p:	d[x] = -1
            for y in sub:
                d[y] += 1
                if not d[y]: del d[y]
            if not d: L.append(i)
        return L
        '''





        '''
        # 359ms 29.51%
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res
        '''




    	'''
    	# 366ms 26.79%
    	a=[]
        l=len(p)
        cp=Counter(p)
        cs=Counter(s[:l-1])
        i=0
        while i+l<=len(s):
            cs[s[i+l-1]]+=1
            if cs==cp:
                a.append(i)
            cs[s[i]]-=1
            if cs[s[i]]==0:
                del cs[s[i]]
            i+=1
        return a
    	'''


    	'''
        # time exceed
        L = []
        for i in xrange(0,len(s)-len(p)+1):
            sub = s[i:i+len(p)]
            same = True
            # for x in set(sub):
            #     if sub.count(x) != p.count(x):
            #         same = False
            for x in xrange(ord("a"),ord("z")+1):
                if sub.count(chr(x)) != p.count(chr(x)):
                    same = False
            if same:
                L.append(i)
        return L
        '''


        '''
        # time exceed
        L = []
        for i in xrange(0,len(s)-len(p)+1):
            sub = s[i:i+len(p)]
            if Counter(sub) == Counter(p):
                L.append(i)
        return L
        '''