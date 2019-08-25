class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        i = 0
        for e in t:
            if i == len(s):
                break
            if e == s[i]:
                print(e)
                i+=1
        return True if i == len(s) else False

sol = Solution()
s1 = "yaojin"
s2 = "dehualiu"
t = "yiiiiaiiiieeeojdfin"
res1 = sol.isSubsequence(s1, t)
res2 = sol.isSubsequence(s2, t)
print("test1:", res1, "test2:", res2)