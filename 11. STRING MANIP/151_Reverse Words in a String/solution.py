class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = " "
        resList = s.split()
        resList = resList[::-1]
        return res.join(resList)