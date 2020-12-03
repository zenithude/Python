#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: zenithude

Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and
previous pointers, it could have a child pointer, which may or may not point
to a separate doubly linked list. These child lists may have one or more
children of their own, and so on, to produce a multilevel data structure,
as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly
linked list. You are given the head of the first level of the list.



Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL

Example 3:

Input: head = []
Output: []



How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

To serialize all levels together we will add nulls in each level to signify
no node connects to the upper node of the previous level. The serialization
becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]

Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]



Constraints:

    Number of Nodes will not exceed 1000.
    1 <= Node.val <= 10^5


"""


class Node(object):
    """List of Nodes Double Linked."""

    def __init__(self, val, prev, next, child):
        """
        Initialize the list.

        Parameters
        ----------
        val : TYPE int
        prev : TYPE int
        next : TYPE int
        child : TYPE int

        Returns
        -------
        None.

        """
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution1:
    """
    DFS traverse and put every nodes inorder to a list.

    then traverse the list and rebuild a single level linked list.
    """
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        nodes = []

        def dfs(node):
            if node is None:
                return
            nodes.append(node)
            if node.child:
                dfs(node.child)
            if node.next:
                dfs(node.next)

        dfs(head)
        head = nodes[0]
        head.child = None
        for i in range(1, len(nodes)):
            node = nodes[i]
            prev = nodes[i - 1]
            node.child = None
            node.prev = prev
            prev.next = node
        return head


class Solution2:
    """
    change it into a preorder binary tree traversal problem: child is the
    left node and next is the right node.
    """
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dummy = Node(-1, None, head, None)

        def dfs(prev, curr):
            if not curr: return prev
            curr.prev = prev
            prev.next = curr
            temp_next = curr.next
            tail = dfs(curr, curr.child)
            curr.child = None
            return dfs(tail, temp_next)

        dfs(dummy, head)
        dummy.next.prev = None
        return dummy.next


class Solution3:
    """
    This is an iteration method.

    Time complexity: O(n)

    Space complexity: O(n)
    """
    def flatten(self, head):
        if head is None:
            return None
        dummy = Node(-1, None, head, None)
        prev = dummy
        stack = [head]

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr
        dummy.next.prev = None
        return dummy.next
