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
        n = len(s)
        p = n - 1
        right = -1
        # e.g.    s = "RoSe Wira??"
        # n = 11
        # p = 10
        while p >= 0:
            if right == -1 and s[p] != ' ':
                right = p # right = 10 
            elif right >= 0 and s[p] == ' ':
                return right - p  # in this case, returns 10 - 4 = 6
            # p decrements until empty space is encountered
            # in this case, p will decrement to 4
            p -= 1

        # if the code can run up to here, that means while loop is
        # finished and no empty space is encountered
        # so return the length of entire string 
        if right >= 0:
            return right + 1
        # else statement deals with empty string scenario
        else:
            return 0

s = Solution()
length1 = s.lengthOfLastWord ("RoSe Wira??")
length2 = s.lengthOfLastWord ("RoSeWira??")
length3 = s.lengthOfLastWord ("       ")
print (length1, length2, length3)
