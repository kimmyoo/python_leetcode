"""
Given two strings s and t, write a function to determine if t is an anagram of
s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d = {}
        for c in s:
            if c in d:
                d[c] += 1 # remember how many occurence of character c
            else:
                d[c] = 1

        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1
                #print (d[c])
            # here we can only see if d[c]<0.
            if d[c] < 0:  
                return False
        return True

#test code
s = Solution()
print(s.isAnagram("niarwi", "ariniw"))
print(s.isAnagram("nij", "inj"))
print(s.isAnagram("funn", "fuun"))
