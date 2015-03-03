"""
https://oj.leetcode.com/problems/lru-cache/

LRU Cache  

Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, 
        otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. 
        When the cache reached its capacity, 
        it should invalidate the least recently used item before inserting a new item.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import rand_list
from support import collections
from support import DoublyLinkedNode, DoublyLinkedList


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self._cache = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        value = self._cache.pop(key, -1)
        if value == -1:
            return -1
            
        self._cache[key] = value
            
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self._cache.pop(key, -1)          
            
        if len(self._cache) >= self.capacity:
            self._cache.popitem(last=False)
            
        self._cache[key] = value
            
    def __str__(self):
        return str(self._cache)
        
    __repr__ = __str__
    

class LRUCache2:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self._cache = {}
        
        self._list = DoublyLinkedList()
               
    # @return an integer
    def get(self, key):
        value = self._cache.get(key, -1)
        if value == -1:
            return -1
            
        val, node = value
        self._move_to_top(node)

        return val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self._cache:
            if len(self._cache) >= self.capacity:
                # remove first one in list and cache
                node = self._list.popleft()
                self._cache.pop(node.value, None)

            node = DoublyLinkedNode(None, None, key)
        else:
            _, node = self._cache[key]
        # insert key to list top
        self._move_to_top(node)
                        
        self._cache[key] = (value, node)

    def _move_to_top(self, node):
        node = self._list.remove(node)
        self._list.push(node)

    def __str__(self):
        return str(self._cache)
        
    __repr__ = __str__
        
        
def test_main():   
    ops = [
        (1, "set(2,1),get(2),set(3,2),get(2),get(3)", [1, -1, 2]),
        (2, "set(2,1),set(1,1),get(2),set(4,1),get(1),get(2),set(1,1),get(4)", [1, -1, 1, -1]),
        (1101, "[set(253,668),set(202,206),set(202, 0),get(465),get(1333),set(651,3249),set(453,2472),get(1050),"
               "set(145,881),set(1256,1320),set(342,1528),get(1256),set(280,2814),get(11),set(878,903),"
               "set(1278,2808),set(942,3238)", [-1, -1, -1, 1320, -1]),
    ]
    for cap, op, res in ops:
        lru = LRUCache2(cap)
        print(op)
        op = op.split("),")
        for o in op:
            if o.startswith("set"):
                lru.set(*[int(p) for p in o.strip("set()").split(",")])
            elif o.startswith("get"):
                r = lru.get(*[int(p) for p in o.strip("get()").split(",")])
                print(r)

        for n in lru._list:
            print(n)

        print(lru._cache)
                
  
if __name__ == "__main__":
    test_main()
