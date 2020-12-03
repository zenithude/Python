# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:16:34 2020

@author: zenithude

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

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


"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.list_element = []

    def get(self, key: int) -> int:
        if key in self.hash.keys():
            del self.list_element[self.list_element.index(key)]
            self.list_element.insert(0, key)
            return self.hash[key]
            
            
        else:
            return -1
        
            

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            self.hash[key] = value
            self.list_element.insert(0, key)
            if len(self.list_element) > self.capacity:
                del self.hash[self.list_element[-1]]
                del self.list_element[-1]
            
        else:
            element_index = self.list_element.index(key)
            self.list_element[:] = self.list_element[:element_index] + self.list_element[element_index + 1:]
            self.list_element.insert(0, key)
            self.hash[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            

