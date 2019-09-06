class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        strList = list(s)
        for i in range(0, len(s), 2*k):
            strList[i: i+k] = strList[i:i+k][::-1]
        return "".join(strList)


s = Solution()
str = "oayjinoayjin"
k = 3
res = s.reverseStr(str, k)
print(res)

