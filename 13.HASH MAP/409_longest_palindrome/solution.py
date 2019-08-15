"""
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes 
that can be built with those letters.
This is case sensitive, 
for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7

hint: if the s is consisted of letter of even number counts or there is 
only one odd number occurance letter, the longest is equal to the length 
of the string. 

if there more than one letters that have odd number occurance, 
the length is equal to len(s) - numOfOdd + 1
1 represents the middle element.
"""
import collections

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        numOfOdd = 0
        
        # learn how to use Counter
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        for k in d:
            if d[k] % 2 == 1:
                numOfOdd += 1
        if numOfOdd > 1:
            res = len(s) - numOfOdd + 1
            return res
        else:
            return len(s)

    #rewrite using Counter()
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        numOfOdd = 0
        #Counter class is added to collections module in python 2.7
        d = collections.Counter(s)

        for k in d:
            if d[k] % 2 == 1:
                numOfOdd += 1
        res = len(s) - numOfOdd + 1 if numOfOdd > 1 else len(s)
        return res


#test
s = Solution()
testString = "cccaabb"
res1 = s.longestPalindrome(testString)
res2 = s.longestPalindrome2(testString)
print(res1, res2)
