#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: zenithude

Given a singly linked list, return a random node's value from the linked
list. Each node must have the same probability of being chosen.

Follow up: What if the linked list is extremely large and its length is
unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should
have equal probability of returning. solution.getRandom();

"""
import random


class ListNode(object):
    """List of Nodes Double Linked."""

    def __init__(self, x):
        """
        Initialize the list.

        Parameters
        ----------
        x : TYPE int

        Returns
        -------
        None.

        """
        self.val = x
        self.next = None
        self.prev = None


def constructListNode(arr):
    """
    Construct ListNode with a List
    :param arr: List()
    :return: ListNode()
    """
    NewListNode = ListNode(arr[0])
    arr.pop(0)
    if len(arr) > 0:
        NewListNode.next = constructListNode(arr)
    return NewListNode


def headLength(head):
    """
    Function return number of Nodes in ListNode().
    :param head: ListNode()
    :return: int
    """
    numberNode = 0
    while head is not None:
        head = head.next
        numberNode += 1
    return numberNode


def listPrint(node):
    print("None", end='<-->')
    while node is not None:
        print(node.val, end='<-->')
        last = node
        node = node.next
    print(node)


class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        n, k = 1, 1
        head, ans = self.head, self.head
        while head.next:
            n += 1
            head = head.next
            if random.random() < k / n:
                ans = ans.next
                k += 1

        return ans.val
