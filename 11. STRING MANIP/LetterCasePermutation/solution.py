"""
Given a string S, we can transform every letter individually to be 
lowercase or uppercase to create another string.  Return a list of all 
possible strings we could create.
Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

"""


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']
        for c in S:
            if c.isalpha():
                res = [s+cur for s in res for cur in [c.lower(), c.upper()]]
            else:
                res = [s+c for s in res]
        return res


s = Solution()
testString = "912Qbc"
res = s.letterCasePermutation(testString)
print(res)
