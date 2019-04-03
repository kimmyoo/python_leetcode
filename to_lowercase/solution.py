class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        #return str.lower()
        strList = [ord (l) for l in str]
        res = ''
        for l in strList:
            if (l >= 65 and l <= 90):
                l +=32
                res += chr(l)
            else:
                res += chr(l)
        return res
 

s = Solution()
lowered = s.toLowerCase("Bull$hit")
print(lowered)


