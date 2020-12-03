# -*- coding: utf-8 -*-
"""
@author : zenithude

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        div = 0
        dummy = tail = ListNode(None)

        while l1 or l2:
            div, mod = divmod(
                    (l1.val if l1 else 0) + (l2.val if l2 else 0) + div, 10)
            tail.next = tail = ListNode(mod)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if div:
            tail.next = ListNode(div)

        return dummy.next


s = Solution()

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)

d.next = e
e.next = f

r = s.addTwoNumbers(a, d)
while r:
    print(r)
    r = r.next
