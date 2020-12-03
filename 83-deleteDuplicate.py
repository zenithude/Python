#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: zenithude


"""


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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        now = head
        cur = head

        while now.next:
            cur = now.next
            if cur.val == now.val:
                now.next = cur.next
            else:
                now = now.next
        return head