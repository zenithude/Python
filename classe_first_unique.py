# -*- coding: utf-8 -*-
"""
@author: zenithude

You have a queue of integers, you need to retrieve the first unique integer
in the queue.

Implement the FirstUnique class:

    FirstUnique(int[] nums) Initializes the object with the numbers in the
    queue. int showFirstUnique() returns the value of the first unique
    integer of the queue, and returns -1 if there is no such integer. void
    add(int value) insert value to the queue.
"""


class FirstUnique:
    def __init__(self, nums):
        self.queue = []
        self.dict = {}
        for element in nums:
            self.add(element)

    def showFirstUnique(self) -> int:
        while len(self.queue) > 0 and self.dict[self.queue[0]] > 1:
            self.queue.pop(0)
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]

    def add(self, value: int) -> None:
        if value in self.dict:
            self.dict[value] += 1
        else:
            self.dict[value] = 1
            self.queue.append(value)


# Your FirstUnique object will be instantiated and called as such:
nums = [2, 3, 5]
obj = FirstUnique(nums)
print(obj.queue)
print(obj.dict)
print(obj.showFirstUnique())
