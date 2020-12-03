# -*- coding: utf-8 -*-
"""
@author : zenithude

Remove K Digits

Given a non-negative integer num represented as a string, remove k digits
from the number so that the new number is the smallest possible.

Note:

    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3 Output: "1219" Explanation: Remove the three
digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1 Output: "200" Explanation: Remove the leading 1
and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2 Output: "0" Explanation: Remove all the digits from
the number and it is left with nothing which is 0.

Initialiser le résultat sous forme de chaîne vide
      res = ""
buildLowestNumber (str, n, res)
1) Si n == 0, alors il n'y a rien à supprimer.
    Ajoutez l'ensemble «str» à «res» et retournez

2) Soit 'len' la longueur de 'str'. Si «len» est plus petit ou égal
    à n, alors tout peut être supprimé
    N'ajoutez rien à «res» et retournez

3) Trouvez le plus petit caractère parmi les premiers (n + 1) caractères
    de «str». Soit l'index du plus petit caractère minIndex.
    Ajoutez «str [minIndex]» à «res» et répétez pour la sous-chaîne après
    minIndex et pour n = n-minIndex

      buildLowestNumber (str [minIndex + 1..len-1], n-minIndex).
"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        longueur = len(num)
        if k >= longueur:
            return '0'
        listN = []
        for i in range(longueur):
            while len(listN) != 0 and k > 0:
                if num[i] < listN[-1]:
                    del listN[-1]
                    k -= 1
                else:
                    break

            if k == 0:
                listN.append(num[i])
            else:
                if i == longueur - 1 or num[i] <= num[i + 1]:
                    listN.append(num[i])
                else:
                    k -= 1

        while len(listN) != 0 and k > 0:
            del listN[-1]
            k -= 1

        if len(listN) > 0:
            while listN[0] == '0':
                del listN[0]
                if len(listN) == 0:
                    return '0'
        res = ''.join(listN)
        if res == '':
            res = '0'
        return res


num = "10"
k = 1
s = Solution()
print(s.removeKdigits(num, k))
