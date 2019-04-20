"""
Write a function that reverses a string. The input string is given as an 
array of characters char[].
Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        halfIndex = len(s) //2
        for i in range (halfIndex):
            s[i], s[-1-i] = s[-1-i], s[i]


