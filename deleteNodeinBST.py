#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zenithude.
Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the
given key in the BST. Return the root node reference (possibly updated) of
the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

"""


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

    def deleteNode(self, root, key):
        if not root: return None

        if root.val == key:
            if not root.right: return root.left

            if not root.left: return root.right

            if root.left and root.right:
                temp = root.right
                while temp.left: temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root

tree = make_tree([4, 2, 7, 1, 3])
obj = Solution()
