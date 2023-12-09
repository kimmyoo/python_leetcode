# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1, str2 = "", ""
        return str1.join(word1) == str2.join(word2)


    # slow compared with the first one 
    # see https://waymoot.org/home/python_string/
    def arrayStringsAreEqual2(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1, str2 = "", ""
        for i in range(len(word1)):
            str1 += word1[i]
        for j in range(len(word2)):
            str2 += word2[j]
        return str1 == str2