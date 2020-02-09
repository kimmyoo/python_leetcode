# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases. e.g.
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome. Note: Have you consider that the 
# string might be empty?  
# This is a good question to ask during an interview. For this problem, 
# we define empty string as valid palindrome.
"""
strategy: two pointers both ends
knowledge point: ch.isalnum()
BIG O analysis: space O(1), time: O(n)
"""
class Solution(object):
    def isPalindrome(self, s):
        """:type s: str
           :rtype: bool
        """
        # take care of empty string
        if not s:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower(): # ignoring cases
                    return False
                left += 1
                right -= 1
            else: # ignoring punctuation
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
        return True

# some tests
s = Solution()
testList = ['winira!r,i,niw', 'bob?', '', 'peep!', 'sad']
for string in testList:
    print (string +':', s.isPalindrome(string))

