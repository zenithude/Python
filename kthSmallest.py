# -*- coding: utf-8 -*-
"""
@author : zenithude
Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up: What if the BST is modified (insert/delete operations) often and
you need to find the kth smallest frequently? How would you optimize the
kthSmallest routine?

"""
"""
To solve this, we will follow these steps −

    -> create one empty list called nodes
    -> call solve(root, nodes)
    -> return k – 1th element of nodes
    -> the solve method is created, this takes root and nodes array, this will 
    work as follows −
    -> if root is null, then return
    -> solve(left of root, nodes)
    -> add value of root into the nodes array
    -> solve(right of root, nodes)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(temp, data):
    que = [temp]
    while len(que):
        temp = que[0]
        que.pop(0)
        if not temp.left:
            temp.left = TreeNode(data)
            break
        else:
            que.append(temp.left)
        if not temp.right:
            temp.right = TreeNode(data)
            break
        else:
            que.append(temp.right)


def make_tree(elements):
    Tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert(Tree, element)
    return Tree


class Solution:
    def kthSmallest(self, root, k):
        """

        :param root: : TreeNode
        :param k: int
        :return: int
        """
        nodes = []
        self.solve(root, nodes)
        return nodes[k - 1]

    def solve(self, root, nodes):
        if root is None:
            return
        self.solve(root.left, nodes)
        nodes.append(root.val)
        self.solve(root.right, nodes)

    def levelOrder(self, root):
        """
        :param root: TreeNode(object)
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

        return result


root = make_tree([3, 1, 4, None, 2])
root1 = make_tree([5, 3, 6, 2, 4, None, None, 1])

s = Solution()
print(s.kthSmallest(root, 1))
print(s.kthSmallest(root1, 3))
print(s.levelOrder(root))
print(s.levelOrder(root1))