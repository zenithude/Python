#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zenithude.
Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

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


class Solution1(object):
    """Object to Test."""

    def zigzagLevelOrder(self, root):
        """

        :param root : TreeNode
        :return: List[List[int]]
        """
        # Base case
        if root is None:
            return

        # Create 2 stacks to store current and next level
        currentLevel, nextLevel = [], []

        # if ltr is True push nodes from left to right otherwise from right
        # to left
        ltr = True

        # append root to currentLevel stack
        currentLevel.append(root)

        # check if stack is empty
        while len(currentLevel) > 0:
            # pop from stack
            temp = currentLevel.pop(-1)
            # print the data
            print(temp.val, " ", end="")

            if ltr:
                if temp.left:
                    nextLevel.append(temp.left)
                if temp.right:
                    nextLevel.append(temp.right)
            else:
                if temp.right:
                    nextLevel.append(temp.right)
                if temp.left:
                    nextLevel.append(temp.left)

            if len(currentLevel) == 0:
                # reverse ltr to push node in oppsite order
                ltr = not ltr
                # swapping of stack
                currentLevel, nextLevel = nextLevel, currentLevel


class Solution(object):
    """Object to Test."""

    def zigzagLevelOrder(self, root):
        """

        :param root : TreeNode
        :return: List[List[int]]
        """
        if not root:
            return []

        queue, result = [root], []
        while queue:
            sublist, levelNum = [], len(queue)

            for i in range(levelNum):
                node = queue.pop(0)
                sublist.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(sublist)
        for i in range(len(result)):
            if i % 2 != 0:
                result[i].reverse()
        return result


list_tree = deserialize('[3,9,20,null,null,15,7]')

print(preorderTraversal(list_tree))

obj = Solution()

print(obj.zigzagLevelOrder(list_tree))



