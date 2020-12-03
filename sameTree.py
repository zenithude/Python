#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zenithude.
Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical
and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false


"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val)) for val in
             string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


def insert(temp, data):
    que = []
    que.append(temp)
    while (len(que)):
        temp = que[0]
        que.pop(0)
        if (not temp.left):
            if data is not None:
                temp.left = TreeNode(data)
            else:
                temp.left = TreeNode(0)
            break
        else:
            que.append(temp.left)
            if (not temp.right):
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

    def isSameTree(self, p, q):
        """
        Check if two TreeNode are similar.

        :param p : TreeNode
        :param q : TreeNode
        :return : Bool
        """
        if not p and not q:
            return True
        if p and q:
            return p.val == q.val and self.isSameTree(p.left,
                                                      q.left) and \
                   self.isSameTree(
                p.right, q.right)
        return False


p = deserialize('[1,2]')
p = make_tree(p)
q = deserialize('[]')
q = make_tree(q)
obj = Solution()
print(obj.isSameTree(p, q))
