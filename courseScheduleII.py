# -*- coding: utf-8 -*-
"""
@author : zenithude

Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] Output: [0,1]
Explanation: There are a total of 2 courses
to take. To take course 1 you should have finished course 0. So the correct
course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation:

There are a total of 4 courses to take. To take course 3 you should have
finished both courses 1 and 2. Both courses 1 and 2 should be taken after
you finished course 0. So one correct course order is [0,1,2,3]. Another
correct ordering is [0,2,1,3] .

Note:

    The input prerequisites is a graph represented by a list of edges,
    not adjacency matrices. Read more about how a graph is represented.

    You may assume that there are no duplicate edges in the input
    prerequisites.

"""


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """

        :param numCourses : int
        :param prerequisites : List[List[int]]
        :return: List[int]
        """
        in_degree, adj = self.create_adj(numCourses, prerequisites)
        visited = [0 for i in range(numCourses)]
        stack = []
        for i in range(numCourses):
            if not visited[i] and not self.dfs(i, visited, stack, adj):
                return []
        return stack[::-1]

    def create_adj(self, n, graph):
        adj = {}
        in_degree = [0 for i in range(n)]
        for i in graph:
            in_degree[i[0]] += 1
            if i[1] in adj:
                adj[i[1]].append(i[0])
            else:
                adj[i[1]] = [i[0]]
        return in_degree, adj

    def dfs(self, node, visited, stack, adj):
        if visited[node] == -1:
            return False
        if visited[node] == 1:
            return True
        visited[node] = -1
        if node in adj:
            for i in adj[node]:
                if not self.dfs(i, visited, stack, adj):
                    return False
        visited[node] = 1
        stack.append(node)
        return True