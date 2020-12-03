# -*- coding: utf-8 -*-
"""
@author : zenithude

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be
changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


"""


class ListNode():
    """List of Nodes."""

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

    def __str__(self):
        """Print the List."""
        return '<ListNode {}>'.format(self.val)


def listPrint(head):
    """
    Print the ListNode passed in params.

    :param head : type ListNode
    :return: nothing just print the Listnode
    """
    while head:
        print(head, end='->')
        head = head.next
    print(head)


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # step 1: find middle
        if not head:
            return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        slow.next = None

        # step 3: merge lists
        head1, head2 = head, prev
        while head2:
            after = head1.next
            head1.next = head2
            head1 = head2
            head2 = after


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()

listPrint(s.reorderList(a))