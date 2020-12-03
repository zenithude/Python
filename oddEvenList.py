# -*- coding: utf-8 -*-
"""
@author : zenithude

Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the
even nodes. Please note here we are talking about the node number and not
the value in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

    The relative order inside both the even and odd groups should remain as
    it was in the input. The first node is considered odd, the second node
    even and so on ...

    L'ordre relatif à l'intérieur des groupes pairs et impairs doit rester
    tel qu'il était dans l'entrée. Le premier nœud est considéré comme
    impair, le deuxième nœud pair et ainsi de suite ...

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        odd, even = [], []
        numberNode = self.headLength(head)
        for i in range(1, numberNode + 1):
            node = head.val
            if i % 2 != 0:
                odd.append(node)
            else:
                even.append(node)
            head = head.next
        print('odd :', odd, 'even :', even)
        odd.extend(even)
        print(odd)
        resultListNode = self.constructResult(odd)
        return resultListNode

    def constructResult(self, result):
        NewListNode = ListNode(result[0])
        result.pop(0)
        if len(result) > 0:
            print('element :', result[0])
            NewListNode.next = self.constructResult(result)
        return NewListNode

    def headLength(self, head):
        numberNode = 0
        while head is not None:
            head = head.next
            numberNode += 1
        return numberNode


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

s = Solution()
sol = (s.oddEvenList(head))

print(type(sol))
while head is not None:
    print(head.val)
    head = head.next

while sol is not None:
    print(sol.val)
    sol = sol.next