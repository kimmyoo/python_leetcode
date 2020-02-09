# Implement strStr().
# Return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.
# if needle is "", return 0
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
            else:
                i+=1
        return -1
    
    def strStrB(self, haystack, needle):
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
res1 = s.strStr("morose", "rose")
res2 = s.strStr("supercalifragelistic", "expialidocious")
print(res1, res2)
