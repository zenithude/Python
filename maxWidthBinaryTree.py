#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zenithude.

Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given
tree. The width of a tree is the maximum width among all levels. The binary
tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the
leftmost and right most non-null nodes in the level, where the null nodes
between the end-nodes are also counted into the length calculation.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4

Explanation: The maximum width existing in the third level with the length 4
(5,3,null,9).

Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2

Explanation: The maximum width existing in the third level with the length 2
(5,3).

Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2

Explanation: The maximum width existing in the second level with the length
2 (3,2).

Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8

Explanation:The maximum width existing in the fourth level with the length 8
(6,null,null,null,null,null,null,7).



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


# Compute the "height" of a tree -- the number of
# nodes along the longest path from the root node
# down to the farthest leaf node.
def height(node):
    if node is None:
        return 0
    else:

        # compute the height of each subtree
        lHeight = height(node.left)
        rHeight = height(node.right)

        # use the larger one
        return (lHeight + 1) if (lHeight > rHeight) else (rHeight + 1)

    # Driver program to test above function


class Solution1(object):
    """Object to Test."""

    def widthOfBinaryTree(self, root):
        """

        :param root : TreeNode
        :return: int
        """
        if root is None:
            return 0

        maxWidth = 0
        h = height(root)
        # Get width of each level and compare the width with the maximum so far
        for i in range(1, h + 1):
            width = self.getWidth(root, i)
            if width > maxWidth:
                maxWidth = width
        return maxWidth

    def getWidth(self, root, level):

        if level == 1:
            return 1
        elif level > 1:
            return (self.getWidth(root.left, level - 1) + self.getWidth(
                    root.right, level - 1))


class Solution(object):
    """Object to Test."""

    def widthOfBinaryTree(self, root):
        """

        :param root : TreeNode
        :return: int
        """

        min_hash, max_hash, best = {}, {}, 0

        def dfs(node, level, index):
            nonlocal best
            if node is None:
                return

            if level in min_hash:
                min_hash[level] = min(min_hash[level], index)
            else:
                min_hash[level] = index

            if level in max_hash:
                max_hash[level] = max(max_hash[level], index)
            else:
                max_hash[level] = index

            best = max(best, max_hash[level] - min_hash[level] + 1)

            dfs(node.left, level + 1, index * 2 + 1)
            dfs(node.right, level + 1, index * 2 + 2)

        dfs(root, 0, 0)

        return best


tree = deserialize('[1,3,2,5,3,null,9]')
tree1 = deserialize('[1,3,null,5,3]')
print(type(tree1))
print(preorderTraversal(tree1))

obj = Solution()
print(obj.widthOfBinaryTree(tree1))
