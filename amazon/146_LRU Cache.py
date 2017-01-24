'''
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up: Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

'''
get(key):
if key exists: Get the value of the key.[pop and insert,so it's been used, actually change it's position in the queue]
otherwise: return -1.

put(key, value):
1. if the key already in it: updated key.[pop and insert, actually change it's position in the queue]
2. if the key not exists,
   2.1 if the cache has capacity: insert the value.
   2.2 if the cache did not has capacity: pop the least recently used item(left item in a queue) before inserting a new item.
'''

import collections

class LRUCache(object):

    # 295 40%
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()    # OrderedDict: dict subclass that remembers the order entries were added
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)   # pop key
        self.dic[key] = v       # insert value
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:                   # if already in the dic, pop and finally insert value;
            self.dic.pop(key)
        else:
            if self.remain > 0:               # if self.dic remains space, decrease the space and insert value;
                self.remain -= 1
            else:
                self.dic.popitem(last=False)  # last=True: return in LIFO(stack)order; last=False: return in FIFO(queue)order.
        self.dic[key] = value



    '''
    # 949 11.23%
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.deque = collections.deque([])
        self.dic = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.dic[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self.deque.remove(key)
        elif len(self.dic) == self.capacity:
            v = self.deque.popleft()  # remove the Least Recently Used element
            self.dic.pop(v)
        self.deque.append(key)
        self.dic[key] = value
    '''


cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print "get(1)",cache.get(1)       # returns 1

cache.put(3,3)                     # evicts key 2
print "get(2)",cache.get(2)       # returns -1 (not found)

cache.put(4,4)                     # evicts key 1
print "get(1)",cache.get(1)       # returns -1 (not found)
print "get(3)",cache.get(3)       # returns 3
print "get(4)",cache.get(4)       # returns 4
