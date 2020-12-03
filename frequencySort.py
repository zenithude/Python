#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: zenprog

Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of
characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.

So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        MAX, seen, counts, result = 0, [], [], []
        for element in s:
            if element not in seen:
                seen.append(element)
                count = s.count(element)
                counts.append(count)
                if MAX < count:
                    MAX = count
        while MAX > 0:
            for i in range(len(counts)):
                if counts[i] == MAX:
                    result.append(seen[i] * MAX)
            MAX -= 1

        return ''.join(result)


obj = Solution()
s = "his s he a ha he  ha ae"
s1 = "Aabb"
print(obj.frequencySort(s))
print(obj.frequencySort(s1))