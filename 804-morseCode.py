# -*- coding: utf-8 -*-
"""
@author : zenithude

804. Unique Morse Code Words
Easy

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of
the Morse code of each letter. For example, "cab" can be written as
"-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll
call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note:

    The length of words will be at most 100.
    Each words[i] will have length in range [1, 12].
    words[i] will only consist of lowercase letters.


"""
import time
import string


class Solution:
    def uniqueMorseRepresentations(self, words):
        """

        :param words : List[str]
        :return : int
        """
        morseCodes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                      "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                      "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                      "-.--", "--.."]
        mapping = dict(zip(string.ascii_lowercase, morseCodes))
        result_set = set()
        for word in words:
            result_set.add(''.join([mapping[i] for i in word]))
        return len(result_set)


class Solution_1:
    def uniqueMorseRepresentations(self, words):
        """

        :param words : List[str]
        :return : int
        """
        c = []
        a = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
             ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
             "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        # take above array from question
        # // ord is used to get ascii value

        for x in words:
            b = ''
            for i in x:
                d = ord(i) - 97
                b = b + a[d]
            if b not in c:
                c.append(b)
        e = len(c)
        return e


start_time1 = time.time()
obj = Solution()
words = ["gin", "zen", "gig", "msg"]
print(obj.uniqueMorseRepresentations(words))
final_time1 = round(time.time() - start_time1, 3)


start_time2 = time.time()
obj = Solution_1()
words = ["gin", "zen", "gig", "msg"]
print(obj.uniqueMorseRepresentations(words))
final_time2 = round(time.time() - start_time2, 3)


print(final_time1, final_time2)