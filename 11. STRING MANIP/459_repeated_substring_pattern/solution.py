"""
Given a non-empty string check if it can be constructed by 
taking a substring of it and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only and 
its length will not exceed 10000.

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)/2):
            if s[:i+1]*(len(s)/(i+1)) == s:
                return True
        return False
    
    # compare with #796 rotate string
    def repeatedSubstringPattern2(self, str):
        return str in (2 * str)[1:-1]

