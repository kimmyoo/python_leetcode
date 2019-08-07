"""
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        smallest = len(s)
        
        d = dict()
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        for k in d:
            if d[k] == 1:
                if s.index(k) < smallest:
                    smallest = s.index(k)
        if smallest < len(s):
            return smallest
        else:
            return -1

