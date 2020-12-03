# -*- coding: utf-8 -*-
"""
@author : zenithude

Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree.

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.



Example 1:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation:
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
Other valid sequences are:
0 -> 1 -> 1 -> 0
0 -> 0 -> 0

Example 2:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

Example 3:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.



Constraints:

    1 <= arr.length <= 5000
    0 <= arr[i] <= 9
    Each node's value is between [0 - 9].

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root, arr):
        """
        :param root: TreeNode()
        :param arr: List(int)
        :return: bool
        """
        if root is None:
            return False
        return self.isPath(root, arr, 0)

    def isPath(self, root, arr, index):
        """
        :param root: TreeNode()
        :param arr: List(int)
        :param index: int
        :return: bool
        """
        if root.val != arr[index]: return False
        if index == len(arr) - 1:
            return root.left is None and root.right is None
        return (root.left is not None and self.isPath(root.left, arr, index + 1)) or (root.right is not None and self.isPath(root.right, arr, index + 1))
        return isPath(root, arr, n, index)