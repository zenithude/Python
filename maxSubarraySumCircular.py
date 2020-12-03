# -*- coding: utf-8 -*-
"""
@author : zenithude

 Maximum Sum Circular Subarray

Given a circular array C of integers represented by A, find the maximum
possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning
of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length,
and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most
once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not
exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

Note:
    -30000 <= A[i] <= 30000
    1 <= A.length <= 30000

"""


class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        k = self.Kadane(A)
        current_sum = 0
        for i in range(len(A)):
            current_sum += A[i]
            A[i] = -A[i]
            
        current_sum = current_sum + self.Kadane(A)

        if current_sum > k and current_sum != 0:
            return current_sum
        else:
            return k

    def Kadane(self, nums):
        best_sum = nums[0]  # or: float('-inf')
        current_sum = nums[0]
        for x in nums[1:]:
            current_sum = max(x, current_sum + x)
            best_sum = max(current_sum, best_sum)
        return best_sum


obj = Solution()
ex_1 = [1, -2, 3, -2]
ex_2 = [5, -3, 5]
ex_3 = [3, -1, 2, -1]
ex_4 = [3, -2, 2, -3]
ex_5 = [-2, -3, -1]

print('sum 1 :', obj.maxSubarraySumCircular(ex_1))
print('sum 2 :', obj.maxSubarraySumCircular(ex_2))
print('sum 3 :', obj.maxSubarraySumCircular(ex_3))
print('sum 4 :', obj.maxSubarraySumCircular(ex_4))
print('sum 5 :', obj.maxSubarraySumCircular(ex_5))
