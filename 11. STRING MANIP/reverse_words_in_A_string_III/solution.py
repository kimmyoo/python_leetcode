"""
Given a string, you need to reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there 
will not be any extra space in the string.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = []
        rs = ''
        for n in range (len(s)):
            if s[n] != ' ':
                stack.append(s[n])
            else:
                while len(stack) > 0:
                    res.append(stack.pop())
                res.append(' ')
        while (len(stack)>0):
            res.append(stack.pop())
        return rs.join(res)
    
    # leetcode solution
    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return ' '.join(s)


s = Solution()
res = s.reverseWords("I don't think you can do it")
print(res)



