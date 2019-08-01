"""
Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
Note:
You may assume the string contains only lowercase alphabets.
"""
import string
class Solution(object):
    def isAnagram1(self, s, t):
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
                d[c] += 1 #if not the first time, update the occurrence of character c
            else: # first time of occurrence of char c
                d[c] = 1

        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1
            # here we can only see if d[c]<0.
            # because the value is supposed to be 0 if they anagrams 
            # if one of the same letter appeared more than it appeared in the first string, 
            # d[c] is less than 0
            if d[c] < 0:  
                return False
        return True

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for e in s:
            if e in d:
                d[e] +=1
        
        for i in t:
            if i in d:
                d[i] -=1
        
        for ele in d:
            if d[ele] != 0:
                return False
        return True
"""
method1 is better than method2. why?
less memory
"""
#test code
s = Solution()
print(s.isAnagram1("niarwi", "ariniw"))
print(s.isAnagram1("nij", "inj"))
print(s.isAnagram1("funn", "fuun"))

print(s.isAnagram2("niarwi", "ariniw"))
print(s.isAnagram2("nij", "inj"))
print(s.isAnagram2("funn", "fuun"))
