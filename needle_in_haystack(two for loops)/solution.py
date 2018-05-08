"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
e.g.
Input: haystack = "hello", needle = "ll"
Output: 2
"""

class Solution():
    def strStr(self, needle, haystack):
        """
        needle: string
        haystack: string
        return type: int
        """
        nl = len(needle)
        hl = len(haystack)
        #     le
        # needle     hl -nl = 4 + 1 = 5    range(5): 0-4
        for k in range (hl- nl + 1):
            matched = True
            for i in range (nl):
                if haystack[k + i] != needle[i]:
                    matched = False
                    break # break control the inner for
            # this if condition is checked hl-nl+1 times
            if matched: 
                return k
        return -1


s = Solution()
res1 = s.strStr("eeeed", "neeeeeeeedle")
res2 = s.strStr("dll", "neeeedle")
print(res1, res2)
