# -*- coding: utf-8 -*-
"""
@author : zenithude
 Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:

    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.


"""
import time


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictWord = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.dictWord
        for element in word:
            if element not in current:
                current[element] = {}
            current = current[element]
        current['#'] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.dictWord
        for element in word:
            if element not in current:
                return False
            current = current[element]
        return '#' in current

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given
        prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.dictWord
        for element in prefix:
            if element not in current:
                return False
            current = current[element]
        return True


# Debut du decompte du temps
start_time = time.time()
trie = Trie()

trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
final_time = round(time.time() - start_time, 5)

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % final_time)