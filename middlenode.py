# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:29:37 2020

@author: zenit
When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast. When fast reaches the end of the list, slow must be in the middle.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

s = Solution()
print(s.middleNode([1,2,3,4,5]))
