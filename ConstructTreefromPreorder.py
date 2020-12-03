#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: zenithude Return the root node of a binary search tree that matches
the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
any descendant of node.left has a value < node.val, and any descendant of
node.right has a value > node.val.  Also recall that a preorder traversal
displays the value of the node first, then traverses node.left,
then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to
find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]



Constraints:

    1 <= preorder.length <= 100
    1 <= preorder[i] <= 10^8
    The values of preorder are distinct.


"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        result = []
        root = None
        while preorder:
            if root is None:
                root, preorder = self.getRoot(preorder)
            left, preorder = self.getLeft(root, preorder)
            right, preorder = self.getRight(root, preorder)
            print(root.val, left.val, right.val)
            print(preorder)
            root.left = left
            root.right = right
            if root not in result:
                result.append(root)
            if left not in result:
                result.append(left)
            if right not in result:
                result.append(right)
            root = left

        return result

    def getRoot(self, preorder):
        if not preorder:
            return None
        root = TreeNode(preorder.pop(0))
        return root, preorder

    def getLeft(self, root, preorder):
        if not preorder:
            return None
        if root is None:
            preorder.pop(0)
            left = None
            return left, preorder
        for i in range(len(preorder)):
            if preorder[i] < root.val:
                left = TreeNode(preorder[i])
                return left, preorder

    def getRight(self, root, preorder):
        if not preorder:
            return None
        right = None
        for i in range(len(preorder)):
            if preorder[i] > root.val:
                right = TreeNode(preorder[i])
                return right, preorder


pre = [8, 5, 1, 7, 10, 12]
result = Solution()
root = result.bstFromPreorder(pre)
print(root)
