# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:32:08 2020

@author: zenit
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.MinStack = []

    def push(self, x: int) -> None:
        self.MinStack.append(x)

    def pop(self) -> None:
        if len(self.MinStack) > 0:
            self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return min(self.MinStack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)