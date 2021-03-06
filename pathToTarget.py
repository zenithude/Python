﻿# -*- coding: utf-8 -*-
"""@author : zenithude

Given a directed, acyclic graph of N nodes.  Find all
possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:

    The number of nodes in the graph will be in the range [2, 15].

    You can print different paths in any order, but you should keep the
    order of nodes inside one path.
--------------------------------------------------------------------------

To solve this, we will follow these steps −

    Make one 2d array called res

    Define a method called solve, this will take graph, node, target and
    temp array

    insert node into temp

    if node is target, then insert temp into res and return

    for i in range 0 to size of graph[node] – 1

        call solve(graph, graph[node, i], target, temp)

    From the main method create array temp, call solve(graph, 0, size of
    graph - 1, temp)

    return res
"""


class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(formed):
            if formed[-1] == n - 1:
                sol.append(formed)
                return
            for child in graph[formed[-1]]:
                dfs(formed + [child])

        sol, n = [], len(graph)
        dfs([0])
        return sol


obj = Solution()
graph = [[1, 2], [3], [3], []]
print(obj.allPathsSourceTarget(graph))