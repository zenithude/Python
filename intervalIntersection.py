#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: zenprog

Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise
disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real
numbers x with a <= x <= b.  The intersection of two closed intervals is a
set of real numbers that is either empty, or can be represented as a closed
interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)



Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,
26]] Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]] Reminder: The
inputs and the desired output are lists of Interval objects, and not arrays
or lists.



Note:

    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

NOTE: input types have been changed on April 15, 2019. Please reset to
èdefault code definition to get new method signature.

"""


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if self.intersect(A[i], B[j]):
                temp = [max(A[i][0], B[j][0]), min(A[i][1], B[j][1])]
                A[i][0] = temp[1] + 1
                B[j][0] = temp[1] + 1
                if A[i][0] > A[i][1] or A[i][1] <= temp[0]:
                    i += 1
                if B[j][0] > B[j][1] or B[j][1] <= temp[0]:
                    j += 1
                result.append(temp)
                continue
            if A[i][0] > B[j][1]:
                j += 1
            else:
                i += 1
        return result

    def intersect(self, a, b):
        if a[0] <= b[0] <= a[1]:
            return True
        if b[0] <= a[0] <= b[1]:
            return True
        return False


obj = Solution()
A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(obj.intervalIntersection(A, B))
