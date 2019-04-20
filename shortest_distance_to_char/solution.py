"""
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        # try to define a value that is really small as prev
        prev = float('-inf')
        for i, c in enumerate(S):
            if c == C:
                prev = i
            res.append(i - prev)
        prev = float('inf')
        #print(res)
        for i in range (len(S)-1, -1, -1):
            if S[i] == C:
                prev = i
            res[i] = min(res[i], prev - i)

        return res
                

s = Solution()
res = s.shortestToChar("hello", 'e')
print(res)
