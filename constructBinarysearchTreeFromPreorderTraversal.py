# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:47:49 2020

@author: zenit

Return the root node of a binary search tree that matches the given preorder 
traversal.

(Recall that a binary search tree is a binary tree where for every node, any 
descendant of node.left has a value < node.val, and any descendant of 
node.right has a value > node.val.  Also recall that a preorder traversal 
displays the value of the node first, then traverses node.left, then 
traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 

    1 <= preorder.length <= 100
    The values of preorder are distinct.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def bstFromPreorder(self, preorder):
        """
        Parameters
        ----------
        preorder : List[int]
        
        Returns
        -------
        TreeNode
        
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        first_right_child_idx = len(preorder)
        for idx, node in enumerate(preorder):           
            if node > root.val:
                first_right_child_idx = idx
                break
        root.left = self.bstFromPreorder(preorder[1:first_right_child_idx])
        root.right = self.bstFromPreorder(preorder[first_right_child_idx:])
        return root
    
s = Solution()
TN = [8,5,1,7,10,12]
s.bstFromPreorder(TN)