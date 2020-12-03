# -*- coding: utf-8 -*-
"""
@author : zenithude

"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[] for i in range(1000)]

    def hash(self, key: int):
        return key % 1000

    def add(self, key: int) -> None:
        hashKey = self.hash(key)
        if not self.contains(key):
            self.arr[hashKey].append(key)

    def remove(self, key: int) -> None:
        hashKey = self.hash(key)
        if self.contains(key):
            self.arr[hashKey].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashKey = self.hash(key)
        return key in self.arr[hashKey]
