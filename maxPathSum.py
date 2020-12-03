# -*- coding: utf-8 -*-
"""
@author: zenithude

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def maxPathSum(self, root):
        """
        Parameters
        ----------
        root : TreeNode()

        Returns
        -------
        int
        """
        stack, color, record, r = [], defaultdict(int), {}, float('-inf')

        while stack or root:
            if root and color[root] < 1:
                stack.append(root)
                root = root.left
            elif color[stack[-1]] < 1:
                color[stack[-1]] += 1
                root = stack[-1].right
            else:
                node = stack.pop()
                color[node] += 1

                left, right = [record.get(c, 0) for c in (node.left, node.right)]

                m = max(node.val, left + node.val, right + node.val)
                r = max([r, m, left + right + node.val] + sum([[record[c]] if c else [] for c in (node.left, node.right)], []))
                record[node] = m

                if stack:
                    color[stack[-1]] += 1
                    root = stack[-1].right
                else:
                    root = None
        return r
