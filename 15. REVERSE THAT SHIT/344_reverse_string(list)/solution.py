"""
Write a function that reverses a string. 
The input string is given as an array of characters char[].
Do not allocate extra space for another array, 
you must do this by modifying the input array           in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        halfIndex = len(s)//2
        for i in range (halfIndex):
            s[i], s[-(1+i)] = s[-(1+i)], s[i]
        return
    
s = Solution()
strA= ["h","e","l","l","o"]
s.reverseString(strA)
print(strA)
strA.reverse()
print(strA)