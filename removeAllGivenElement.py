#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: zenithude

Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5



"""


class ListNode(object):
    """List of Nodes Linked."""

    def __init__(self, val=0, nextval=None):
        """
        Initialize the list.

        Parameters
        ----------
        val : TYPE int
        nextval : Type int

        Returns
        -------
        None.

        """
        self.val = val
        self.nextval = None


def constructListNode(arr):
    """
    Construct ListNode with a List
    :param arr: List()
    :return: ListNode()
    """
    NewListNode = ListNode(arr[0])
    arr.pop(0)
    if len(arr) > 0:
        NewListNode.nextval = constructListNode(arr)
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
        node = node.nextval
    print(node)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        """

        :param head : ListNode
        :param val: int
        :return : ListNode
        """
        if not head:
            return
        factice = ListNode(float('-inf'))
        factice.nextval = head
        previous, current = factice, factice.nextval

        while current:
            if current.val == val:
                previous.nextval = current.nextval
            else:
                previous = current
            current = current.nextval

        return factice.nextval

arr = [1, 2, 6, 3, 4, 5, 6]
head = constructListNode(arr)
obj = Solution()
listPrint(obj.removeElements(head, 6))