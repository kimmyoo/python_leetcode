"""
Implement strStr().
Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, needle, haystack):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

          needle:             | m |
        haystack: |   n - m   | m |,   0 -> n-m +1
        """
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            #looking for a break point 
            #if no break, a total match is found, return i. 
            for k in range(m):
                if haystack[i + k] != needle[k]:
                    break
            # IMPORTANT: for, else statements 
            # this else will be executed
            # only if the above for loop is completed m times
            else:
                return i
        return -1


s = Solution()
res1 = s.strStr("rose", "morose")
res2 = s.strStr("supercalifragelistic", "expialidocious")
print(res1, res2)
