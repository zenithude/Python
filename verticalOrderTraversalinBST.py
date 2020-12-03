#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zenithude.
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively
will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the
vertical line touches some nodes, we report the values of the nodes in order
from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is
reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report
will have a list of values of nodes.



Example 1:

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:

Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:

The node with value 5 and the node with value 6 have the same position
according to the given scheme.

However, in the report "[1,5,6]", the node value of 5 comes first since 5 is
smaller than 6.
Note:

    The tree will have between 1 and 1000 nodes.
    Each node's value will be between 0 and 1000.
"""
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val)) for val in
             string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def insert(temp, data):
    que = [temp]
    while len(que):
        temp = que[0]
        que.pop(0)
        if not temp.left:
            if data is not None:
                temp.left = TreeNode(data)
            else:
                temp.left = TreeNode(0)
            break
        else:
            que.append(temp.left)
            if not temp.right:
                if data is not None:
                    temp.right = TreeNode(data)
                else:
                    temp.right = TreeNode(0)
                break
            else:
                que.append(temp.right)


def make_tree(elements):
    Tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert(Tree, element)
    return Tree


def inorderTraversal(root):
    """
    Left -> Root -> Right
    :param root: TreeNode()
    :return: List[int]
    """
    res = []
    if root:
        res = inorderTraversal(root.left)
        res.append(root.val)
        res = res + inorderTraversal(root.right)
    return res


def postorderTraversal(root):
    """
    Left -> Right -> Root
    :param root: TreeNode()
    :return: List[int]
    """
    res = []
    if root:
        res = postorderTraversal(root.left)
        res = res + postorderTraversal(root.right)
        res.append(root.val)
    return res


def preorderTraversal(root):
    """
    Root -> Left ->Right
    :param root: TreeNode()
    :return: List[int]
    """
    res = []
    if root:
        res.append(root.val)
        res = res + preorderTraversal(root.left)
        res = res + preorderTraversal(root.right)
    return res


def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

        # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

        # Key is smaller than root's key
    return search(root.left, key)


class Solution(object):
    """Object to Test."""

    def __init__(self):
        self.min_1, self.max_1 = float("inf"), -float("inf")

    def verticalTraversal(self, root):
        """

        :param root : TreeNode()
        :return : List[List[int]]
        """
        dt = defaultdict(list)

        def dfs(root, lvl_h, lvl_v):
            self.min_1 = min(lvl_h, self.min_1)
            self.max_1 = max(lvl_v, self.max_1)
            dt[lvl_h].append((lvl_v, root.val))
            if root.left:
                dfs(root.left, lvl_h - 1, lvl_v + 1)
            if root.right:
                dfs(root.right, lvl_h + 1, lvl_v + 1)

        dfs(root, 0, 0)
        out = []
        for i in range(self.min_1, self.max_1 + 1):
            out += [[j for i, j in sorted(dt[i])]]

        return out


tree = deserialize('[3,9,20,null,null,15,7]')
tree2 = deserialize('[1,2,3,4,5,6,7]')
obj = Solution()
print(obj.verticalTraversal(tree))
print(obj.verticalTraversal(tree2))
