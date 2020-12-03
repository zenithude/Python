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


# A O(n) program for construction of BST from preorder traversal 
  
INT_MIN = float("-infinity") 
INT_MAX = float("infinity") 
  
# A Binary tree node 
class Node: 
  
    # Constructor to created a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Methods to get and set the value of static variable 
# constructTreeUtil.preIndex for function construcTreeUtil() 
def getPreIndex(): 
    return constructTreeUtil.preIndex 
  
def incrementPreIndex(): 
    constructTreeUtil.preIndex += 1 
  
# A recursive function to construct BST from pre[]. 
# preIndex is used to keep track of index in pre[] 
def constructTreeUtil(pre, key, mini, maxi, size): 
      
    # Base Case 
    if(getPreIndex() >= size): 
        return None
  
    root = None
      
    # If current element of pre[] is in range, then  
    # only it is part of current subtree 
    if(key > mini and key < maxi): 
  
        # Allocate memory for root of this subtree  
        # and increment constructTreeUtil.preIndex 
        root = Node(key) 
        incrementPreIndex() 
  
        if(getPreIndex() < size): 
             
            # Construct the subtree under root  
            # All nodes which are in range {min.. key} will 
            # go in left subtree, and first such node will  
            # be root of left subtree 
            root.left = constructTreeUtil(pre, 
                         pre[getPreIndex()], mini, key, size) 
  
            # All nodes which are in range{key..max} will 
            # go to right subtree, and first such node will 
            # be root of right subtree 
            root.right = constructTreeUtil(pre, 
                     pre[getPreIndex()], key, maxi, size) 
  
    return root 
  
# This is the main function to construct BST from given 
# preorder traversal. This function mainly uses 
# constructTreeUtil() 
def constructTree(pre): 
    constructTreeUtil.preIndex = 0 
    size = len(pre) 
    return constructTreeUtil(pre, pre[0], INT_MIN, INT_MAX, size) 
  
  
# A utility function to print inorder traversal of Binary Tree  
def printInorder(node): 
      
    if node is None: 
        return 
    printInorder(node.left) 
    print (node.data,)
    printInorder(node.right) 
  
  
# Driver program to test above function 
pre = [10, 5, 1, 7, 40, 50] 
root = constructTree(pre) 
  
print ("Inorder traversal of the constructed tree: ")
printInorder(root) 