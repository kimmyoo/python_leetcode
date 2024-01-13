"""
You are given two strings of the same length s and t. 
In one step you can choose any character of t and replace it 
with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same 
characters with a different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" 
which is anagram of s.


        # hint: 1. Count the frequency of characters of each string.
        # Loop over all characters if the frequency of a character 
        # in t is less than the frequency of the same character in s 
        # then add the difference between the frequencies to the answer.
"""

import collections

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        extra = 0
        counterS = collections.Counter(s)
        counterT = collections.Counter(t)
        for k in counterT:
            if k in counterS:
                if counterT[k] > counterS[k]:
                    extra += counterT[k] - counterS[k]
            else:
                extra += counterT[k]
                # here counterS[k] is 0
                # extra += counterT[k] - counterS[k]
        return extra

s = Solution()
res = s.minSteps("leetcode", "practice")
print(res)