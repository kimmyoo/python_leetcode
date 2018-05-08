"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

For example, Given s = "Hello World",
return 5.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #if s is an empty string, len(s) is 0; i is -1
        i = len(s) - 1
        #skip all white spaces starting from the end of the string
        while i >= 0 and s[i].isspace():
            i -= 1

        res = 0
        while i >= 0 and not s[i].isspace():
            res += 1
            i -= 1
        return res

s = Solution()
length1 = s.lengthOfLastWord ("who's RoSe Wira??    ")
length2 = s.lengthOfLastWord ("        ")
print (length1, length2)
