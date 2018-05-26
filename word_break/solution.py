"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.
For example, given
s = "leetcode",
dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        t = [False for i in range(n)]# a list of boolean values of False
        for i in range(n):
            # learn how to use string slicing in this way
            if s[:i + 1] in wordDict:
                t[i] = True # t[i] indicates s[:i + 1] is such a string
            else:
                #variable j in this for loop double verifies the previous matching
                for j in range(i):
                    if t[j] is True and s[j + 1:i + 1] in wordDict:
                        t[i] = True
                        break
        return t[-1]# last line is brilliant. If a total match couldn't 
        # be found, the last item in the t[] list must be false; if a 
        # total match is found, the last item in the list must be True.
s = Solution()
dict = ["eyes", "can", "talk", "gut", "feeling"]
print (s.wordBreak("feelingeyescantalk", dict))
