class Solution(object):
    #my solution
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res, j = [], 0
        nString = S.replace("-", '')#get rid of '-'
        l = len(nString)
        #reformatting string into a list in reversed order
        for i in range(l):
            ch = nString[l-i-1]
            if ch.isalnum():
                ch = ch.upper()
                res.append(ch)
                j+=1
            if j % K == 0:
                res.append('-')
        #this is an edge case for res is an empty list caused by eg. S = "------"
        if res:
            if res[-1] == '-':
                del res[-1]
        res.reverse()
        ans = ''.join(res)
        return ans

s = Solution()
S = "5F3Z-2e-9-w"
K = 4
res = s.licenseKeyFormatting(S, K)
print(res)