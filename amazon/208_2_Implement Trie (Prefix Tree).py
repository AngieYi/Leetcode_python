'''
208. Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.
Note: You may assume that all inputs are consist of lowercase letters a-z.
'''

# a trie, also called digital tree, radix tree or prefix tree

# 458ms, 37%
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for ch in word:
            cur = cur.children[ch]  # current node is always updated
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for ch in word:
            '''
            cur = cur.children.get(ch)
            if not cur:               # if cur is None, then it did not has children attribute
                return False
            '''
            if ch not in cur.children:  # this way is more efficient than the previous way
                return False
            cur = cur.children[ch]
        return cur.is_word              # False: word ends in the middle of a real word/ True:it's a real word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for ch in prefix:
            '''
            cur = cur.children.get(ch)
            if not cur:                 # if cur is None, then it did not has children attribute
                return False
            '''
            if ch not in cur.children:  # this way is more efficient than the previous way
                return False
            cur = cur.children[ch]
        return True                     # all True: word ends in the middle or at the end of a real word

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)